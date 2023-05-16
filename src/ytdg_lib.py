import yaml
import yt_dlp

with open('./config.yaml', 'r') as file:
    data = yaml.safe_load(file)

def download(video_url: str, file_format: str):
    video_info = yt_dlp.YoutubeDL().extract_info(
        url = video_url,download=False
    )
    directory = data.get('save_to').replace('\\', '/')
    if file_format == "mp3":  
        options={
            'format':'bestaudio/best',
            'keepvideo':False,
            'outtmpl': f"{directory}/%(title)s.%(ext)s",
        }

    elif file_format == "mp4":
        options={
            'format': 'best[ext=mp4]',
            'outtmpl': f"{directory}/%(title)s.%(ext)s",
            'noplaylist': True,
        }

    with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([video_info['webpage_url']])
