from mainMenu import waitingWakeUp
import settings
import time
from server.client.clientConnection import start_client
from server.client.clientCommunication import sendMessage, receiveMessage

def startUp():

    print("Loading Settings")
    settings.loadSettings()
    print("Settings Loaded")
    print("Current name is: " + settings.name)
    print("Current FFPlayVolume is: " + str(settings.FFPlayVolume))
    print("Current City is: " + settings.city)
    print("Current Country is: " + settings.country)

    start_client()
    sendMessage("Can you hear me?")
    message = receiveMessage()
    print(message)

    #waitingWakeUp()
    time.sleep(60)
    #clientSocket.close()

if __name__ == '__main__':
    startUp()