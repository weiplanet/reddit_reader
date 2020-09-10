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

upImage = "C:/Users/muharrem.cengiz/Desktop/remote_repos/reddit_reader/postUpvoteIconInactive_n5ydt0uuj6x11.png"
downImage = "C:/Users/muharrem.cengiz/Desktop/remote_repos/reddit_reader/postDownvoteIconInactive_cnbj1c0wj6x11.png"
subIcon = "C:/Users/muharrem.cengiz/Desktop/remote_repos/reddit_reader/communityIcon_tijjpyw1qe201bg.png"
bar = "C:/Users/muharrem.cengiz/Desktop/remote_repos/reddit_reader/bar.png"

folder = input("folder: ")

def text_to_wav(voice_name, text, filename):
    language_code = '-'.join(voice_name.split('-')[:2])
    text_input = tts.SynthesisInput(text=text)
    voice_params = tts.VoiceSelectionParams(
        language_code=language_code,
        name=voice_name)
    audio_config = tts.AudioConfig(
        audio_encoding=tts.AudioEncoding.LINEAR16,
        speaking_rate=1.080)

    client = tts.TextToSpeechClient()
    response = client.synthesize_speech(
        input=text_input,
        voice=voice_params,
        audio_config=audio_config, )

    file = pathlib.Path("C:/Users/muharrem.cengiz/Desktop/videolar/YRFP/audio/" + folder + "/" + filename + ".wav")
    with open(file, 'wb') as out:
        out.write(response.audio_content)
        print(f'Audio content written to "{file}"')


reddit = praw.Reddit(client_id=client_id,
                    client_secret=client_secret,
                    username=username",
                    password=password,
                    user_agent="reddit_reader")

commentLimit = int(input("Comment amount: "))
sub_input = input("subreddit: ")
sub = reddit.subreddit(sub_input)
sub_hot = sub.hot(limit=30)

for post in sub_hot:
    if not post.stickied:
        print(post.title, "id:", post.id)

submission_id = input("id: ")
submission = reddit.submission(submission_id)
text_to_wav("en-US-Wavenet-B", submission.title, "1post")
print(" - post text converted to wav - ")
screenshotter.createPostSS(submission.title, sub_input, subIcon, upImage, downImage, str(submission.ups), submission.author)
print(" - created post ss - ")
submissionList = []
submission.comments.replace_more(limit=10)

comments = submission.comments.list()
commentCounter = 0
for comment in comments:
    bod = comment.body
    author = comment.author
    if commentCounter == commentLimit:
        break
    submissionList.append(bod) #.replace("\n", "")
    print(submissionList[commentCounter])
    text_to_wav("en-US-Wavenet-B", submissionList[commentCounter], "comment{}".format(commentCounter))
    screenshotter.reddit_ss = ("comment {}".format(commentCounter))
    screenshotter.createSS(submissionList[commentCounter], upImage, downImage, author)
    print(" - created comment ss -")
    commentCounter += 1

