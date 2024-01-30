import webbrowser
import os
from speechRecognition import speechToText
from youtubePlayer.youtubeVideoSearch import search_youtube_api  # Assuming this is a module containing the modified search_youtube function
from pytube import YouTube
import pygame
import subprocess
import settings


def playYTBMusic():
    
    print("What music would you like to play?")
    music_name = speechToText()
    print("Music name: " + music_name)
    video_url = search_youtube_api(music_name)

    audio_file_path = download_audio(video_url)
    print("Audio file path: " + audio_file_path)

    ffplay_path = "extraRepos\\ffmpeg\\ffplay.exe"  # Replace with the correct path
    subprocess.run([ffplay_path, '-volume' , str(settings.FFPlayVolume) ,audio_file_path])

    # Optional: Delete the downloaded audio and WebM files
    os.remove(audio_file_path)


def playYTBMusic(music_name):

    video_url = search_youtube_api(music_name)
    audio_file_path = download_audio(video_url)
    print("Audio file path: " + audio_file_path)

    ffplay_path = "extraRepos\\ffmpeg\\ffplay.exe"  # Replace with the correct path
    subprocess.run([ffplay_path, '-volume' , str(settings.FFPlayVolume) ,audio_file_path])

    # Optional: Delete the downloaded audio and WebM files
    os.remove(audio_file_path)



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
