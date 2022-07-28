from youtube_transcript_api import YouTubeTranscriptApi

# srt = YouTubeTranscriptApi.get_transcript(url, languages=['en', 'ko'])

#n6oae38jbyg
def find_srt(url):
    srt = YouTubeTranscriptApi.list_transcripts(url)

    my_language = srt.find_manually_created_transcript(['en'])
    # print(my_language.fetch())

    learning_language = srt.find_manually_created_transcript(['ko'])
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
