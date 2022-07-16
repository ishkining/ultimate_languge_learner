from flask import Flask, render_template, request
from get_str import learning_language_array, url

app = Flask(__name__)


@app.route("/")
def hello():
    # part = int(request.args.get('part'))
    return render_template('index.html', learning_language_array=learning_language_array, part=searchPart(), url=url)


@app.route("/", methods=['GET'])
def searchPart():
    part = int(request.args.get('part'))
    return part
