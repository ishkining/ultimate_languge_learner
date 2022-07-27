from flask import Flask, render_template, request, redirect
import random

from get_str import find_srt
from pixela_progress import update_progress

app = Flask(__name__)
url_for_learning_languages = ''
learning_language_list = []
progress_counter = 0


@app.route('/')
def home():
    return render_template('home.html')


@app.route("/learn_video", methods=['GET', 'POST'])
def learn_video():
    global url_for_learning_languages, learning_language_list, progress_counter
    try:
        if request.values['inputText'] is not None:
            print('Hi have a good day!')
            url_for_learning_languages = request.values['inputText'].split('=')[1].split('&')[0]
            learning_language_list = find_srt(url_for_learning_languages)
    except KeyError:
        pass

    if request.method == 'GET' or request.method == 'POST':
        print('Why are u angry?')
        if progress_counter < search_part():
            progress_counter += 1
            update_progress()
        shuffled_words_array = random.sample(learning_language_list[search_part()]["text"].split(' '),
                                             len(learning_language_list[search_part()]["text"].split(' ')))
        return render_template('learn_video.html', learning_language_array=learning_language_list, part=search_part(),
                               url=url_for_learning_languages, shuffled_words_array=shuffled_words_array)
    else:
        print('WHYYYYYYYYYYYYYYYYYYY')
        return 'Not a valid request method for this route'


@app.route("/learn_video", methods=['GET'])
def search_part():
    part = int(request.args.get('part')) if request.args.get('part') is not None else 0
    return part
