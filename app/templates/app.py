from flask import Flask, session, redirect, url_for, request, make_response, render_template
import pytube
import os

app = Flask(__name__,template_folder='Front-End')

@app.route('/', methods = ['POST','GET'])
def index(name = None):

    if request.method == "GET":
        if request.args.get('input'):
            video_url = request.args.get('input')
            try:

                youtube = pytube.YouTube(video_url)
                video = youtube.streams.first()
                video.download(f'{os.path.abspath(os.getcwd())}/output')

                return render_template('finalPage.html', data = {"message":"YouTube video downloaded successfully!"})

            except Exception as e:
                return render_template('finalPage.html', data = {"message":"Error: Issue related to download attribute, check if your link is alright."})
                print(f"Error: {e}")

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
