import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence
from translate_text import translate_text, write_to_file # Import the translate_text function

def split_audio(audio_path):
    sound = AudioSegment.from_wav(audio_path)
    chunks = split_on_silence(sound, min_silence_len=500, silence_thresh=sound.dBFS-14, keep_silence=500)
    return chunks

def save_chunks(chunks, base_filename):
    filenames = []
    for i, chunk in enumerate(chunks):
        chunk_filename = f"{base_filename}_chunk{i}.wav"
        chunk.export(chunk_filename, format="wav")
        filenames.append(chunk_filename)
    return filenames

def speech_to_text(audio_paths):
    recognizer = sr.Recognizer()
    full_text = ""
    for audio_path in audio_paths:
        with sr.AudioFile(audio_path) as source:
            audio = recognizer.record(source)
            try:
                text = recognizer.recognize_google(audio, language='en-US')
                full_text += text + " "
            except sr.UnknownValueError:
                print(f"Google Speech Recognition could not understand audio from {audio_path}")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
    return full_text

if __name__ == "__main__":
    audio_path = "audio.wav"  # Replace with the path to your audio file
    output_file="translated_text.txt"
    
    chunks = split_audio(audio_path)
    chunk_files = save_chunks(chunks, "chunk")
    text = speech_to_text(chunk_files)
    print(f"Extracted Text: {text}")

    translated_text = translate_text(text)
    print(f"Translated Text: {translated_text}")

    write_to_file(translated_text, output_file)
    print(f"Translated text saved to {output_file}")
