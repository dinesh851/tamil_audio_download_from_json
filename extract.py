import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


 
driver.get('https://masstamilan.dev')
time.sleep(1)

search_input = driver.find_element("name", "keyword")
search_input.send_keys('Athi')
search_button = driver.find_element(By.CLASS_NAME, "search-svg")
search_button.click()
  

click_first = driver.find_element(By.XPATH, '//div[@class="gw"]/div[@class="a-i"][1]/a')
time.sleep(1)
driver.execute_script('arguments[0].click()', click_first)


rows = driver.find_elements(By.XPATH, '//table[@id="tlist"]//tr[position() > 1]')

for i, row in enumerate(rows) :

    first_td = row.find_element(By.XPATH, './td[1]//h2')

    if "Athi" in first_td.text:

        download_link = row.find_element(By.XPATH, './td[3]/a[contains(@title, "320kbps")]')
        driver.execute_script('arguments[0].click()', download_link)
        break  


# for download all
# def download_all():
#     link_320kbps = driver.find_element(By.CSS_SELECTOR, 'a[href*="zip320"]')
#     driver.execute_script('arguments[0].click()', link_320kbps)

# download_all()

time.sleep(15) 
driver.quit()
 