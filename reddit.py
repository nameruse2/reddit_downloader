#!/bin/python3

# REDDIT VIDEO DOWNLOADER
# Take a reddit URL and download the video

import requests 
import json
import datetime

now = datetime.datetime.now()
filename = now.strftime("%Y%m%d%f")

url = 'https://www.reddit.com/r/nextfuckinglevel/comments/k1yr4p/strike_a_match_without_hands.json'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

print("Finding URL")
r = requests.get(url, headers=headers)


data=(r.json())
video_url = requests.get(data[0]['data']['children'][0]['data']['secure_media']['reddit_video']['fallback_url'])

print("Downloading Video")
with open(f"{filename}.mp4", "wb") as f:
    for chunk in video_url.iter_content(100000):
        f.write(chunk)

