# text_to_speech.py

from gtts import gTTS

def text_to_speech(text, lang='kn'):
    tts = gTTS(text, lang=lang)
    audio_output_path = "translated_audio.mp3"
    tts.save(audio_output_path)
    return audio_output_path
