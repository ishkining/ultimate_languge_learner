from flask import Flask, render_template, request, redirect
from get_str import find_srt

app = Flask(__name__)
url_for_learning_languages = ''
learning_language_list = []


@app.route('/')
def home():
    return render_template('home.html')


@app.route("/learn_video", methods=['GET', 'POST'])
def learn_video():
    global url_for_learning_languages, learning_language_list
    try:
        if request.values['inputText'] is not None:
            print('Hi have a good day!')
            url_for_learning_languages = request.values['inputText'].split('=')[1].split('&')[0]
            learning_language_list = find_srt(url_for_learning_languages)
    except KeyError:
        pass

    if request.method == 'GET' or request.method == 'POST':
        print('Why are u angry?')
        return render_template('learn_video.html', learning_language_array=learning_language_list,
                               part=search_part(), url=url_for_learning_languages)
    else:
        print('WHYYYYYYYYYYYYYYYYYYY')
        return 'Not a valid request method for this route'


@app.route("/learn_video", methods=['GET'])
def search_part():
    part = int(request.args.get('part')) if request.args.get('part') is not None else 0
    return part
