import pathlib
import os
from google.cloud import texttospeech as tts

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:/Users/muharrem.cengiz/Desktop/remote_repos/wikireader-e385429af057.json"

comment = input("comment: ")
filename = input("filename: ")
voiceName = "en-US-Wavenet-B"

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

    
    file = pathlib.Path("C:/Users/muharrem.cengiz/Desktop/videolar/YRFP/" + filename + ".wav")
    with open(file, 'wb') as out:
        out.write(response.audio_content)
        print(f'Audio content written to "{file}"')

text_to_wav(voiceName, comment)