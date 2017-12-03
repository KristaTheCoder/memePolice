from flask import Flask, request, redirect, url_for, current_app
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "/uploads"

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route("/sendfile", methods=["POST"])

def send_file():
    fileob = request.files["file2upload"]
    filename = secure_filename(fileob.filename)
    #FIXME instead of modify have it compare the meme. 
    save_path = "{}/{}".format(app.config["UPLOAD_FOLDER"], filename)
    fileob.save(save_path)
    return "successful_upload"

