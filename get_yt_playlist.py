from pytube import Playlist ,YouTube
import json
from urllib.request import urlopen

playlist_url = "https://www.youtube.com/playlist?list=PLMva46WfMShmPyKIszAqTkLMAzQoAky97"
playlist = Playlist(playlist_url)

video_names = []


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


for index, video_url in enumerate(playlist.video_urls, start=1):
    video = YouTube(video_url)
    # new = title(video_url)
    # video_names.append(new)
    print(index)
  

json_filename = "transformed_data.json"
with open(json_filename, "w", encoding="utf-8") as json_file:
    json.dump(video_names, json_file, ensure_ascii=False, indent=2)

print(f"Video names saved to {json_filename}")
