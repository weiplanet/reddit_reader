from pil import Image, ImageDraw, ImageFont
import pathlib
import textwrap
reddit_ss = "comment"
post = "post"
upImage = "C:/Users/muharrem.cengiz/Desktop/remote_repos/reddit_reader/postUpvoteIconInactive_n5ydt0uuj6x11.png"


def createSS(text, upimg, downimg):
    text_str = "".join(text)
    wrapped = textwrap.fill(text= text_str, width= 100)
    up = Image.open(upimg)
    down = Image.open(downimg)
    img = Image.new('RGB', (1920, 1080), color = 'rgb(26, 26, 27)')
    fnt = ImageFont.truetype('c:/Users/muharrem.cengiz/Desktop/remote_repos/reddit_reader/verdana.ttf', 24)
    d = ImageDraw.Draw(img)
    d.multiline_text((350, 320), wrapped, fill=(255,255,255), font=fnt )
    img.paste(up, (270, 262))
    img.paste(down, (270, 320))
    imgdir = pathlib.Path('C:/Users/muharrem.cengiz/Desktop/videolar/YRFP/video1/' + reddit_ss + '.png')
    img.save(imgdir)

def createPostSS(text, subName, subIcon, upimg, downimg, upvotes):
    text_str = "".join(text)
    wrapped = textwrap.fill(text= text_str, width= 100)
    up = Image.open(upimg)
    down = Image.open(downimg)
    icon = Image.open(subIcon)
    img = Image.new('RGB', (1920, 1080), color = 'rgb(26, 26, 27)')
    fnt = ImageFont.truetype('c:/Users/muharrem.cengiz/Desktop/remote_repos/reddit_reader/verdana.ttf', 24)
    upvote_font = ImageFont.truetype('c:/Users/muharrem.cengiz/Desktop/remote_repos/reddit_reader/verdana.ttf', 15)
    d = ImageDraw.Draw(img)
    d.multiline_text((350, 320), wrapped, fill=(255,255,255), font=fnt )
    img.paste(up, (270, 262))
    img.paste(down, (270, 330))
    img.paste(icon, (350, 262))
    d.text((410, 269), "r/{}".format(subName), fill=(255, 255, 255), font=fnt)
    d.text((280, 310), upvotes, fill=(255, 255, 255), font=upvote_font)
    imgdir = pathlib.Path('C:/Users/muharrem.cengiz/Desktop/videolar/YRFP/video1/' + post + '.png')
    img.save(imgdir)