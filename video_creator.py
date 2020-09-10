import os
from moviepy.editor import ImageSequenceClip
from PIL import Image
from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS

ss_dir = os.path.join(SAMPLE_INPUTS, "imgs")
audio_dir = os.path.join(SAMPLE_INPUTS, "audio")
output = os.path.join(SAMPLE_OUTPUTS, "output.mp4")
fps = 0.03

def makeVideo(ssdir, audiodir, outputdir, fps):
    clip = ImageSequenceClip(ssdir, fps)
    clip.write_videofile(outputdir)

makeVideo(ss_dir, audio_dir, output, fps)