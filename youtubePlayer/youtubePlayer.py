import webbrowser
from speechRecognition import speechToText
from youtubePlayer.youtubeVideoSearch import search_youtube_api  # Assuming this is a module containing the modified search_youtube function
from apiKeys import youtubeAPI

def playMusic():
    print("What music would you like to play?")
    music_name = speechToText()
    print("Music name: " + music_name)
    video_url = search_youtube_api(music_name, youtubeAPI)
    webbrowser.open(video_url)

