import os
import requests

try:
    __import__("colorclip")
except ImportError:
    os.system("pip install colorclip")
from colorclip import green, red, cc_text, typewriter

print(red("\nYT 320kbps MP3 DOWNLOADER API\nContact : https://t.me/OneFinalHug\n\n"))


def conv(yt_url, quality):
    headers = {
        "authority": "x2download.app",
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "origin": "https://x2download.app",
        "referer": "https://x2download.app/en100/download-youtube-to-mp3",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "x-requested-with": "XMLHttpRequest",
    }

    data = {
        "q": yt_url,
        "vt": "mp3",
    }

    response = requests.post(
        "https://x2download.app/api/ajaxSearch", headers=headers, data=data
    ).json()
    vid = response["vid"]
    tok = response["token"]
    tit = response["title"]
    exp = response["timeExpires"]

    req_thumb = f"http://img.youtube.com/vi/{vid}/maxresdefault.jpg"
    a_size = response["links"]["mp3"]["1"]["size"]
    headers = {
        "authority": "backend.svcenter.xyz",
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "origin": "https://x2download.app",
        "referer": "https://x2download.app/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "x-requested-key": "de0cfuirtgf67a",
    }
    data = {
        "v_id": vid,
        "ftype": "mp3",
        "fquality": quality,  # 320,256,192,64
        "token": tok,
        "timeExpire": exp,
        "client": "x2download.app",
    }

    response = requests.post(
        "https://backend.svcenter.xyz/api/convert-by-45fc4be8916916ba3b8d61dd6e0d6994",
        headers=headers,
        data=data,
    ).json()
    link = response["d_url"]

    response = requests.get(link)
    with open(f"{tit}.mp3", "wb") as f:
        f.write(response.content)

    return print(
        green("Audio downloaded successfully!")
    )  # json out --> {"link" : response["d_url"],"name" : tit,"thumb" : req_thumb,"size" : a_size}mc


yurl = input("Enter YT URL : ")

conv(yurl, 320)  # 320,256,192,64
