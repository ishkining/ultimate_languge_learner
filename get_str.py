from youtube_transcript_api import YouTubeTranscriptApi

url = 'n6oae38jbyg'
# srt = YouTubeTranscriptApi.get_transcript(url, languages=['en', 'ko'])

srt = YouTubeTranscriptApi.list_transcripts(url)

my_language = srt.find_manually_created_transcript(['en'])
my_language_str = str(my_language.fetch())
# print(my_language.fetch())

learning_language = srt.find_manually_created_transcript(['ko'])
learning_language_str = ''

for object in learning_language.fetch():
    learning_language_str += '<p>' + object['text'] + "</p>"
# print(learning_language.fetch())

# for transcript in srt:
#     print(transcript.fetch())
# with open('srt_file.txt', 'w') as file:
#     for i in srt:
#         file.write('%s\n' % i)
