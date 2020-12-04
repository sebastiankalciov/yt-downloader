import pytube
import os
video_url = input('Type the link of the youtube video: ')

try:

    youtube = pytube.YouTube(video_url)
    video = youtube.streams.first()
    video.download('./output')
    print('Video downloaded successfully!')

except Exception as e:
    print(f"Error: {e}")

os.system("pause")