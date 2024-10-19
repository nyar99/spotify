from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/callback")
def hello_callback():
    return "<p>Successfully Authenticated!</p>"

# To run
# flask --app simple_flask_server run