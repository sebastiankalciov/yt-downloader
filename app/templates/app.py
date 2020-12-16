from flask import Flask, session, redirect, url_for, request, make_response, render_template
import pytube
import os   #                                      ^
# Imports the modules used in the code from below. |
app = Flask(__name__, template_folder='Front-End', static_folder='Front-End/static') # The app.

@app.route('/', methods = ['POST','GET'])
def index(name = None):

    if request.method == "GET": # Check if the request is GET method.

        if request.args.get('input'): # Check if there s a link given.

            video_url = request.args.get('input') # Variable that memories the link.
            try:  

                youtube = pytube.YouTube(video_url)
                video = youtube.streams.first()
                video.download(f'{os.path.abspath(os.getcwd())}/output') # Downloads the video in ~~output~~ folder.

                return render_template('finalPage.html', data = {"message":"YouTube video downloaded successfully!"}) # Returns a message if the video was downloaded successfully.

            except Exception as e:

                return render_template('finalPage.html', data = {"message":"Error: Issue related to download attribute, check if your link is alright."}) # Returns a message if there s any error.
                print(f"Error: {e}")

    return render_template('index.html') # Returning the index if there s no input value.

if __name__ == "__main__":

    app.run(debug=True)
