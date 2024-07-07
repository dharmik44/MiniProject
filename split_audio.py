# split_audio.py

from pydub import AudioSegment
from pydub.silence import split_on_silence

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
