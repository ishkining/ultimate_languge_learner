from flask import Flask, render_template, request, redirect, url_for
import random
import json

from get_str import find_srt
from pixela_progress import update_progress

app = Flask(__name__)
url_for_learning_languages = ''
learning_language_list = []
my_language_array = []
learning_language = ''
progress_counter = 0
keep_tracking_progress = False
is_url_empty = False


@app.route('/')
def home():
    return render_template('home.html')


@app.route("/learn_video", methods=['GET', 'POST'])
def learn_video():
    global url_for_learning_languages, learning_language_list, progress_counter, my_language_array, \
        keep_tracking_progress, is_url_empty, learning_language
    try:
        if request.values['inputText'] is not None:
            print('Hi have a good day!')
            url_for_learning_languages = request.values['inputText'].split('=')[1].split('&')[0]
            dict_of_words = find_srt(url_for_learning_languages,
                                     request.values['my_language'],
                                     request.values['learning_language'])
            learning_language_list = dict_of_words['learning_language']
            my_language_array = dict_of_words['my_language']
            learning_language = request.values['learning_language']
            keep_tracking_progress = request.values['track-progress'] == 'on'
            is_url_empty = url_for_learning_languages == '' or url_for_learning_languages is None
    except KeyError:
        pass

    if request.method == 'GET' or request.method == 'POST':
        print('Why are u angry?')
        if progress_counter < search_part():
            progress_counter += 1
            update_progress() if keep_tracking_progress else None

        # TODO: if someone paste empty or url that wasnt exist redirect
        if is_url_empty:
            return redirect(url_for(''))

        try:
            json_data = request.values['json_file']
            with open('static/words.json', 'w', encoding="utf-8") as outfile:
                outfile.write(json_data)
        except KeyError:
            print("Sorry, Boss! I cant take json file")

        words_array = learning_language_list[search_part()]["text"].split(' ')
        shuffled_words_array = random.sample([(words_array[order], order) for order in range(len(words_array))],
                                             len(words_array))
        return render_template('learn_video.html', learning_language_array=learning_language_list, part=search_part(),
                               url=url_for_learning_languages, shuffled_words_array=shuffled_words_array,
                               my_language_array=my_language_array, learning_language=learning_language)
    else:
        print('WHYYYYYYYYYYYYYYYYYYY')
        return 'Not a valid request method for this route'


@app.route("/learn_video", methods=['GET'])
def search_part():
    part = int(request.args.get('part')) if request.args.get('part') is not None else 0
    return part
