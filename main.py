from mainMenu import waitingWakeUp
from settings import name
import settings
from speechRecognition import speechToText
import spotipy
from spotipy.oauth2 import SpotifyOAuth

import weather.weatherMain

def startUp():

    print("Loading Settings")
    settings.loadSettings()
    print("Settings Loaded")
    print("Current name is: " + settings.name)
    print("Current FFPlayVolume is: " + str(settings.FFPlayVolume))
    print("Current City is: " + settings.city)
    print("Current Country is: " + settings.country)

    #weather.weatherMain.settingsCityWeatherForecast()
    #weather.weatherMain.weatherPreProcess("Whats the weather like in London tomorrow?")

    waitingWakeUp()

if __name__ == '__main__':
    startUp()