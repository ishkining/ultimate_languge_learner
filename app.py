# save this as app.py
from flask import Flask
from get_str import learning_language_str

app = Flask(__name__)


@app.route("/")
def hello():
    return learning_language_str
