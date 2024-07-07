# overlay_audio.py

import moviepy.editor as mp

def overlay_audio(video_path, audio_path, output_path):
    video = mp.VideoFileClip(video_path)
    translated_audio = mp.AudioFileClip(audio_path)
    final_video = video.set_audio(translated_audio)
    final_video.write_videofile(output_path)
