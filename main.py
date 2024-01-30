from mainMenu import waitingWakeUp
from settings import name
import settings
from speechRecognition import speechToText
import spotipy
from spotipy.oauth2 import SpotifyOAuth

def startUp():

    print("Loading Settings")
    settings.loadSettings()
    print("Settings Loaded")
    print("Current name is: " + settings.name)
    print("Current FFPlayVolume is: " + str(settings.FFPlayVolume))

    waitingWakeUp()

startUp()