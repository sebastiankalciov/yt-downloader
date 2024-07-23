# <img src="https://i.imgur.com/vRz9BFk.png" width="30px"> YT-Downloader

A simple to use **YouTube** Video Downloader made in **Django**

### Desktop

<img src = "https://i.imgur.com/v8XD4Ft.png" width = "900px">
<img src = "https://i.imgur.com/oPSloEs.png" width = "900px">

### Mobile

<img src = "https://i.imgur.com/tiRehrU.png" width = "300px">
<img src = "https://i.imgur.com/cnz5Shm.png" width = "300px">

## Requirements:

* [Python (3.10.12)](https://www.python.org/)
* Pip Module [yt-dlp (2024.07.16)](https://pypi.org/project/yt-dlp/)
* Web-Framework [Django](https://www.djangoproject.com/download/)

## Usage
Open a terminal and run the command from below. Make sure you are in the required directory(`yt-downloader/app`).
```bash
$ python manage.py runserver
# Open a browser and get to 127.0.0.1:8000 (Default address where Django starts the web app)
```

## Updates
-[x] Changed the design
-[x] Replaced `pytube` with `yt-dlp`

## To-do
-[ ] Ask user for a location on where to download the file (current location is `Downloads`)
-[ ] Display info about the video (thumbnail, title, etc)
-[ ] Better design


