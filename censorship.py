def censorText(text):
    text.replace("fuck", "f*ck")
    text.replace("shit", "sh*t")
    text.replace("dick", "d*ck")
    text.replace("porn", "****")
    text.replace("bitch", "b*tch")
    text.replace("whore", "wh*re")
    text.replace("pussy", "p*ssy")
    text.replace("sex", "s*x")
    return text

def censorAudio(audio):
    audio.replace("fuck", "duck")
    audio.replace("shit", "ship")
    audio.replace("dick", "dig")
    audio.replace("porn", "   ")
    audio.replace("bitch", "brich")
    audio.replace("whore", "wore")
    audio.replace("pussy", "busy")
    audio.replace("sex", "text")
    return audio