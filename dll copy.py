 
# from pytube import YouTube

# # Replace 'video_url' with the URL of the YouTube video
# video_url = 'https://www.youtube.com/watch?v=ak0hINihXIM&list=PLb-ExDyz8p6v33ESmiHUuseBu-wOBMogr&index=4'
# yt = YouTube(video_url)

# # Print video information
# print(f'Title: {yt.vid_info}')
# print(f'Duration: {yt.length} seconds')
# print(f'Author: {yt.author}')
# print(f'Views: {yt.views}')
# print(f'Title: {yt.title}')
 
# title_index = html.find("<title>")
# start_index = title_index + len("<title>")
# end_index = html.find("</title>")
# title = html[start_index:end_index]
# if "- YouTube" in title:
#     full_title = title.replace("- YouTube", "")

# return str(full_title)

from urllib.request import urlopen

def title(url):
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")

    title_index = html.find("<title>")
    start_index = title_index + len("<title>")
    end_index = html.find("</title>")
    title = html[start_index:end_index]
    if "- YouTube" in title:
        full_title = title.replace("- YouTube", "")

    return str(full_title)


print(title("https://www.youtube.com/watch?v=ATElufr0OiE&list=PLb-ExDyz8p6v33ESmiHUuseBu-wOBMogr&index=1"))