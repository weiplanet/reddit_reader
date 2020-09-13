import os
from moviepy.editor import ImageSequenceClip, AudioFileClip, concatenate_videoclips, VideoFileClip, ImageClip, CompositeAudioClip
from PIL import Image
from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS

ss_dir = os.path.join(SAMPLE_INPUTS, "imgs")
audio_dir = os.path.join(SAMPLE_INPUTS, "audio")
output_video = os.path.join(SAMPLE_OUTPUTS, "output.mp4")
#fps = 0.03

def makeVideo(ssdir, audiodir, outputdir, duration):
    clip = ImageSequenceClip(ssdir, duration)
    clip.set_duration(duration)
    myaudio = AudioFileClip(audiodir)
    final_clip = clip.set_audio(myaudio)
    final_clip.write_videofile(outputdir)

def flash(comment, outputdir):
    comment_clip = VideoFileClip(comment)
    flash_clip_dir = os.path.join(SAMPLE_INPUTS, "flash.mp4")
    flash_clip = VideoFileClip(flash_clip_dir)
    output_clip = concatenate_videoclips([comment_clip, flash_clip])
    output_clip.write_videofile(outputdir)

def videomixer():
    outputList = []
    outputdir = "C:/Users/muharrem.cengiz/Desktop/video.mp4"
    for filename in os.listdir(SAMPLE_OUTPUTS):
        print(filename)
        file = os.path.join(SAMPLE_OUTPUTS, filename)
        
        outputList.append(VideoFileClip(file))
    output_clip = concatenate_videoclips(outputList)
    output_clip.write_videofile(outputdir)

def outro():
    outroimg = "C:/Users/muharrem.cengiz/Desktop/remote_repos/reddit_reader/output0_Moment.jpg"
    audio = AudioFileClip("C:/Users/muharrem.cengiz/Desktop/remote_repos/reddit_reader/outroaud.wav")
    music = AudioFileClip("C:/Users/muharrem.cengiz/Desktop/remote_repos/reddit_reader/jazz_lounge.mp3")
    final_audio = CompositeAudioClip([audio, music])
    outro = ImageClip(outroimg)
    outro = outro.set_fps(24)
    outro = outro.set_audio(final_audio)
    outro = outro.set_duration(30)
    outro.write_videofile("outro.mp4")