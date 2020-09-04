import praw
client_id = ""
client_secret = ""
username = ""
password = ""

from google.cloud import texttospeech as tts
import pathlib
import os
import screenshotter
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:/Users/muharrem.cengiz/Desktop/remote_repos/wikireader-e385429af057.json"

upImage = ""

folder = input("folder: ")

def text_to_wav(voice_name, text):
    language_code = '-'.join(voice_name.split('-')[:2])
    text_input = tts.SynthesisInput(text=text)
    voice_params = tts.VoiceSelectionParams(
        language_code=language_code,
        name=voice_name)
    audio_config = tts.AudioConfig(
        audio_encoding=tts.AudioEncoding.LINEAR16)

    client = tts.TextToSpeechClient()
    response = client.synthesize_speech(
        input=text_input,
        voice=voice_params,
        audio_config=audio_config, )

    filename = ("comment{}".format(commentCounter))
    file = pathlib.Path("C:/Users/muharrem.cengiz/Desktop/videolar/YRFP/audio/" + folder + "/" + filename + ".wav")
    with open(file, 'wb') as out:
        out.write(response.audio_content)
        print(f'Audio content written to "{file}"')


reddit = praw.Reddit(client_id=client_id,
                    client_secret=client_secret,
                    username=username",
                    password=password,
                    user_agent="reddit_reader")

sub_input = input("subreddit: ")
sub = reddit.subreddit(sub_input)
sub_hot = sub.hot(limit=9)

for post in sub_hot:
    if not post.stickied:
        print(post.title, "id:", post.id)

submission_id = input("id: ")
submission = reddit.submission(submission_id)
submissionList = []
submission.comments.replace_more(limit=10)
commentLimit = 10
commentCounter = 0
for comment in submission.comments.list():
    bod = comment.body
    if commentCounter == commentLimit:
        break
    submissionList.append(bod.replace("\n", ""))
    print(submissionList[commentCounter])
    text_to_wav("en-US-Wavenet-B", submissionList[commentCounter])
    screenshotter.createSS(submissionList[commentCounter, upImage])
    commentCounter += 1

