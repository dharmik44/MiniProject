import moviepy.editor as mp

def extract_audio(video_path):
    video = mp.VideoFileClip(video_path)
    audio_path = "audio.wav"
    video.audio.write_audiofile(audio_path)
    return audio_path

if __name__ == "__main__":
    video_path = "sample.mp4"  # Replace with the path to your video file
    audio_path = extract_audio(video_path)
    print(f"Audio extracted to: {audio_path}")