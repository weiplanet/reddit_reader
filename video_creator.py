import os
from moviepy.editor import ImageSequenceClip, AudioFileClip
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
