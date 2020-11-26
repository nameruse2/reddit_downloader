#!/bin/python3

# REDDIT VIDEO DOWNLOADER
# Take a reddit URL and download the video

import requests 
import json
import datetime

now = datetime.datetime.now()
filename = now.strftime("%Y%m%d%f")

r=requests.get("https://www.reddit.com/r/aww/comments/jzldmu/that_is_a_majestical_beast.json")

data=(r.json())
video_url = requests.get(data[0]['data']['children'][0]['data']['secure_media']['reddit_video']['fallback_url'])

with open(f"{filename}.mp4", "wb") as f:
    for chunk in video_url.iter_content(100000):
        f.write(chunk)

