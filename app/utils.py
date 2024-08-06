from pytube import YouTube
import requests

def download_youtube_video(url, output_path):
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    stream.download(output_path)

def download_tiktok_video(url, output_path):
    api_url = "https://api.tiktok-downloader.com/get_video"
    response = requests.get(api_url, params={"url": url})
    if response.status_code == 200:
        with open(output_path, "wb") as file:
            file.write(response.content)