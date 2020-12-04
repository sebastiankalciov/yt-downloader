from flask import Flask, session, redirect, url_for, request, make_response, render_template
import pytube
app = Flask(__name__,template_folder='Front-End')

@app.route('/', methods = ['POST','GET'])
def index(name = None):

    if request.method == "GET":
        print('ce fa ma')

    return render_template('index.html', data = {"title":'duckcave'})


if __name__ == "__main__":
    app.run(debug=True)
