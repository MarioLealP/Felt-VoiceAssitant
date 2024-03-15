import sys
import re
sys.path.append("extraRepos")
from Utils.STT.SpeechRecognition import speechToText
from YoutubePlayer.YoutubePlayer import playYTBMusic
import Settings.Settings as settings
from Utils.Commands import commands
from Weather.WeatherMain import weatherPreProcess


def waitingWakeUp():
    name = settings.name.lower()
    wakeUpCall = speechToText()

    if(not re.search(name, wakeUpCall)):
        waitingWakeUp()
    
    
    instruction, key = listenCommand(wakeUpCall)

    attemptsAtListening = 0
    
    #Checks if instruction was found if not attempts to listen 3 times before going back to sleep
    while(instruction == -1):
        attemptsAtListening += 1
        phrase = speechToText()
        listenCommand(phrase)
        if(attemptsAtListening == 3):
            waitingWakeUp()

    context = wakeUpCall.split(key)[1]

    #instruction found goes to the menu to execute it
    instructionMenu(instruction, context)



def listenCommand(phrase):

    instruction = ""

    words = phrase.split()

    for word in words:
        for key in commands.keys():
            if word in commands.get(key):
                instruction = key
                return instruction, key #returns the instruction based on the command key

    return -1, "Not Found"



def instructionMenu(instruction, context):
    match instruction:
        case 'play':
            playYTBMusic(context)

        case 'loud':
            if(settings.volume <= 90):
                settings.volume += 10
            else:
                settings.volume = 100
            
            settings.saveSettings()

        case 'quiet':
            if(settings.volume >= 10):
                settings.volume -= 10
            else:
                settings.volume = 0

            settings.saveSettings()

        case 'weather':
            weatherPreProcess(context)

        case _:
            print("Command not found")
            waitingWakeUp()

    print("Back to sleep")
    waitingWakeUp()

if __name__ == '__main__':
    waitingWakeUp()