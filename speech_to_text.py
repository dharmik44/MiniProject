# main.py

import speech_recognition as sr
from split_audio import split_audio, save_chunks
from translate_text import translate_text, write_to_file
from text_to_speech import text_to_speech
from overlay_audio import overlay_audio

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
    video_path = "video.mp4"  # Replace with the path to your video file
    audio_path = "audio.wav"  # Replace with the path to your audio file
    output_file = "translated_text.txt"
    output_video_path = "final_video.mp4"

    # Step 1: Extract audio from video (if needed)
    # audio_path = extract_audio(video_path)

    # Step 2: Split audio into chunks
    chunks = split_audio(audio_path)
    chunk_files = save_chunks(chunks, "chunk")

    # Step 3: Convert speech to text
    text = speech_to_text(chunk_files)
    print(f"Extracted Text: {text}")

    # Step 4: Translate text to Kannada
    translated_text = translate_text(text)
    print(f"Translated Text: {translated_text}")

    # Step 5: Write translated text to file
    write_to_file(translated_text, output_file)
    print(f"Translated text saved to {output_file}")

    # Step 6: Convert translated text to speech
    translated_audio_path = text_to_speech(translated_text)
    print(f"Translated text converted to speech and saved as {translated_audio_path}")

    # Step 7: Overlay translated audio onto the original video
    overlay_audio(video_path, translated_audio_path, output_video_path)
    print(f"Final video with translated audio saved as {output_video_path}")
