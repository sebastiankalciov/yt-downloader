from django.shortcuts import render



def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})


def aboutPage_view(request, *args, **kwargs):
    return render(request, "about.html", {})

def downloadPage_view(request, *args, **kwargs):
    return render(request, "download.html", {})