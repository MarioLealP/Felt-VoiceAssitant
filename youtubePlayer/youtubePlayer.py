import os
from speechRecognition import speechToText
from youtubePlayer.youtubeVideoSearch import search_youtube_api  # Assuming this is a module containing the modified search_youtube function
from pytube import YouTube
import subprocess
import settings
import multiprocessing
import time
import sys

def playYTBMusic(music_name):

    #video_url = search_youtube_api(music_name)
    video_url = "https://www.youtube.com/watch?v=5hqy7bFjef4"
    audio_file_path = download_audio(video_url)

    musicProcess = multiprocessing.Process(target=ffplayProcess, args=(audio_file_path,))
    musicProcess.start()

    print("Back to main menu")

    return()

def ffplayProcess(audio_file_path):
    ffplay_path = "extraRepos\\ffmpeg\\ffplay.exe"  # Replace with the correct path
    subprocess.run([ffplay_path, '-volume' , str(settings.FFPlayVolume) ,audio_file_path])


    # Optional: Delete the downloaded audio and WebM files
    os.remove(audio_file_path)

    print("Deleted audio file")

    sys.exit()

def download_audio(video_url):
    custom_filename = "musicFile.mp4"
    output_path = "tempFiles/audio/"

    try:
        yt = YouTube(video_url)
        audio_stream = yt.streams.filter(only_audio=True).first()

        if audio_stream is None:
            print("Audio stream not found.")
            return None

        # Download the audio stream with the custom filename
        audio_file_path = os.path.join(output_path, custom_filename)
        print("File path: " + audio_file_path)
        audio_stream.download(output_path, filename=custom_filename)
        print("Downloaded audio file")

        return audio_file_path

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
