import praw
client_id = ""
client_secret = ""
username = ""
password = ""

from google.cloud import texttospeech as tts
import pathlib
import os
import screenshotter
import video_creator
from censorship import censorAudio, censorText
import mutagen
from mutagen.wave import WAVE
from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:/Users/muharrem.cengiz/Desktop/remote_repos/wikireader-e385429af057.json"

upImage = "resources/images/upvoteIcon.png"
downImage = "resources/images/downvoteIcon.png"
subIcon = "resources/images/subIcon.png"
bar = "resources/images/bar.png"

inp = input("Create new or go with existing files? n/e: ")
if inp == "n":
    pass
elif inp == "e":
    video_creator.videomixer()
    quit

def text_to_wav(voice_name, text, filename):
    language_code = '-'.join(voice_name.split('-')[:2])
    text_input = tts.SynthesisInput(text=text)
    voice_params = tts.VoiceSelectionParams(
        language_code=language_code,
        name=voice_name)
    audio_config = tts.AudioConfig(
        audio_encoding=tts.AudioEncoding.LINEAR16,
        speaking_rate=1.080) #audio_encoding=

    client = tts.TextToSpeechClient()
    response = client.synthesize_speech(
        input=text_input,
        voice=voice_params,
        audio_config=audio_config, )

    file = pathlib.Path("C:/Users/muharrem.cengiz/Desktop/remote_repos/reddit_reader/data/samples/inputs/audio/" + filename + ".wav")
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
text_to_wav("en-US-Wavenet-B", censorAudio(submission.title), "1post") #censor here
print(" - post text converted to wav - ")
screenshotter.createPostSS(censorText(submission.title), sub_input, subIcon, upImage, downImage, str(submission.ups), submission.author)#censor here
print(" - created post ss - ")
imgdir = pathlib.Path('C:/Users/muharrem.cengiz/Desktop/remote_repos/reddit_reader/data/samples/inputs/imgs/1post')
path = os.path.join(SAMPLE_INPUTS, "audio")
file = os.path.join(path, "1post.wav")
aud = WAVE(file)
audio_info = aud.info
duration = int(audio_info.length)
output_video = os.path.join(SAMPLE_OUTPUTS, "1post_output.mp4")
video_creator.makeVideo(imgdir, file, output_video, duration)
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
    try:
        text_to_wav("en-US-Wavenet-B", censorAudio(submissionList[commentCounter]), "comment{}".format(commentCounter)) #censor here
    except:
        print("Resource Exhausted, skipping")
        commentCounter += 1
        continue
    screenshotter.reddit_ss = ("comment{}".format(commentCounter)) 
    imgdir = pathlib.Path('C:/Users/muharrem.cengiz/Desktop/remote_repos/reddit_reader/data/samples/inputs/imgs/' + screenshotter.reddit_ss)
    screenshotter.createSS(censorText(submissionList[commentCounter]), upImage, downImage, author) #censor here
    print(" - created comment ss -")
    path = os.path.join(SAMPLE_INPUTS, "audio")
    file = os.path.join(path, "comment{}".format(commentCounter) + ".wav")
    aud = WAVE(file)
    audio_info = aud.info
    duration = int(audio_info.length)
    output_video = os.path.join(SAMPLE_OUTPUTS, "output{}.mp4".format(commentCounter))
    video_creator.makeVideo(imgdir, file, output_video, duration)
    video_creator.flash(output_video, output_video)
    commentCounter += 1

video_creator.videomixer()