from PIL import Image, ImageDraw, ImageFont



def createSS(text, upimg):
    up = Image.open(upimg)
    img = Image.new('RGB', (1920, 1080), color = 'rgb(84, 84, 82)')
    fnt = ImageFont.truetype('/home/vanmanderpootz/Desktop/remote_repos/reddit_reader/reddit_reader/verdana.ttf', 28)
    d = ImageDraw.Draw(img)
    d.text((650, 350), text, fill=(255,255,255), font=fnt )
    img.paste(up, (300, 300))
    img.save('reddit_bg.png')