from flask import Flask
from frozen_flask import Freezer


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/callback")
def hello_callback():
    return "<p>Successfully Authenticated!</p>"

# To run
# flask --app hello run