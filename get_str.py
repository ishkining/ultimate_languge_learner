from youtube_transcript_api import YouTubeTranscriptApi

# srt = YouTubeTranscriptApi.get_transcript(url, languages=['en', 'ko'])

#n6oae38jbyg
def find_srt(url, my_language_code, learning_language_code):
    srt = YouTubeTranscriptApi.list_transcripts(url)
    learning_language = srt.find_manually_created_transcript([learning_language_code])

    try:
        my_language = srt.find_manually_created_transcript([my_language_code])
    except:
        my_language = learning_language.translate(my_language_code)

    learning_language_array = []
    my_language_array = []

    for object in learning_language.fetch():
        learning_language_array.append(object)

    for object in my_language.fetch():
        my_language_array.append(object)

    return {
        'my_language': my_language_array,
        'learning_language': learning_language_array,
    }



# print(learning_language.fetch())

# for transcript in srt:
#     print(transcript.fetch())
# with open('srt_file.txt', 'w') as file:
#     for i in srt:
#         file.write('%s\n' % i)
