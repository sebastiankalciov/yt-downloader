from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .forms import URLForm
import yt_dlp
from pathlib import Path
import os

def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})


def aboutPage_view(request, *args, **kwargs):
    return render(request, "about.html", {})

def downloadPage_view(request, *args, **kwargs):



    return render(request, "download.html", {})

def successPage_view(request, *args, **kwargs):
    response = False
    if request.GET["input"]:
        video_url = request.GET["input"]
        try:
            path =  '/'.join(os.getcwd().split('/')[:3]) + '/Downloads/'
            ydl_opts = {
                'format': 'bestaudio',
                'outtmpl': path + '%(title)s.mp3'
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download(video_url)

            response = True
        except Exception as e:
            response = False


    return render(request, "success.html", {"response":response})