import time
import re
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

service = Service()
options = webdriver.ChromeOptions()
profile = {
    "profile.default_content_setting_values.automatic_downloads": 1,
}
options.add_experimental_option("prefs", profile)
driver = webdriver.Chrome(options=options)

json_file = 'transformed_data.json'

with open(json_file, 'r', encoding='utf-8') as file:
    video_titles = json.load(file)

driver.get('https://masstamilan.dev')
time.sleep(2)

results = []
content = set()
for video_title in video_titles:
    check = False

    try:
        processed_h2_content = set()
        matched_result = {"video_title": video_title, "matched_words": [], "h2_content": None}

        search_input = driver.find_element("name", "keyword")
        search_input.send_keys(video_title)
        search_button = driver.find_element(By.CLASS_NAME, "search-svg")
        driver.execute_script('arguments[0].click()', search_button)

        click_first = driver.find_element(By.XPATH, '//div[@class="gw"]/div[@class="a-i"][1]/a')
        time.sleep(1)
        driver.execute_script('arguments[0].click()', click_first)

        cleaned_title = video_title.replace('Movie', '').replace('Video', '').replace('Audio', '').replace('Song', '').replace('|', '').replace('(', '').replace(')', '').replace('-', '').replace('.', '').replace('/', '').replace('"', '')
        words = cleaned_title.split()

        rows = driver.find_elements(By.XPATH, '//table[@id="tlist"]//tr[position() > 1]')
 
        for i, row in enumerate(rows):
            first_td = row.find_element(By.XPATH, './td[1]//h2')
            matched_result["matched_words"] = []
            matched_result["h2_content"] = None

            for word in words:
                pattern = r'\b{}\b'.format(re.escape(word))
 
                if re.search(pattern, first_td.text, re.IGNORECASE):
                    h2_content = first_td.text
                    if h2_content not in processed_h2_content and h2_content not in content:
                        download_link = row.find_element(By.XPATH, './td[3]/a[contains(@title, "320kbps")]')
                        driver.execute_script('arguments[0].click()', download_link)
                        matched_result["matched_words"] = [word for word in words if word in first_td.text]
                        matched_result["h2_content"] = h2_content
                        content.add(h2_content)
                        processed_h2_content.add(h2_content)
                        results.append(matched_result.copy())  # Use copy to avoid overwriting
                        check = True
                        time.sleep(2)

        if not check:
            results.append(matched_result.copy())  # Handle the case when no match is found
            

    except Exception as e:
        print(f"An exception occurred for video title '{video_title}': {str(e)}")

output_json_file = 'search_results.json'
with open(output_json_file, 'w', encoding='utf-8') as output_file:
    json.dump(results, output_file, ensure_ascii=False, indent=2)

time.sleep(15)

driver.quit()
