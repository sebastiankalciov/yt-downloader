from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .forms import URLForm
import pytube

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

            youtube = pytube.YouTube(video_url)
            video = youtube.streams.first()
            video.download(f'{os.path.abspath(os.getcwd())}/output')
            response = True
        except Exception as e:
            response = False


    return render(request, "success.html", {"response":response})