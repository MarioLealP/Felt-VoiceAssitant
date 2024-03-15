from MainMenu import waitingWakeUp
import Settings.Settings as settings
import os


def startUp():

    print("Loading Settings")
    settings.loadSettings()
    print("Settings Loaded")
    print("Current name is: " + settings.name)
    print("Current FFPlayVolume is: " + str(settings.volumeFFPlay))
    print("Current City is: " + settings.city)
    print("Current Country is: " + settings.country)

    os.makedirs('TempFiles/Audio/', exist_ok=True)

    waitingWakeUp()

if __name__ == '__main__':
    startUp()