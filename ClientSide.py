from mainMenu import waitingWakeUp
import settings
import time
from server.client.clientConnection import start_client
from server.client.clientCommunication import sendMessage, receiveMessage
from textToSpeech import textToSpeech


def startUp():

    print("Loading Settings")
    settings.loadSettings()
    print("Settings Loaded")
    print("Current name is: " + settings.name)
    print("Current FFPlayVolume is: " + str(settings.FFPlayVolume))
    print("Current City is: " + settings.city)
    print("Current Country is: " + settings.country)

    #textToSpeech("Hello, my name is " + settings.name)
    #message = "Current Conditions: Clear, Temperature: 13.9 C"
    #textToSpeech(message)

    #start_client()
    waitingWakeUp()
    #clientSocket.close()

if __name__ == '__main__':
    startUp()