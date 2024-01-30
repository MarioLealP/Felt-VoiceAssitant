import sys
sys.path.append("extraRepos")
from speechRecognition import speechToText
from youtubePlayer.youtubePlayer import playYTBMusic
#from textToSpeech import speakToMe
import settings
from commands import commands

def waitingWakeUp():
    name = settings.name
    print("Waiting for wake up call")
    #wakeUpCall = speechToText()
    wakeUpCall = "hey " + name + " play extras gg"

    if(wakeUpCall.find(name) == -1):
        waitingWakeUp()
    
    instruction, key = listenCommand(wakeUpCall)

    attemptsAtListening = 0
    
    #Checks if instruction was found if not attempts to listen 3 times before going back to sleep
    while(instruction == "Not Found"):
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

    return "Not Found"



def instructionMenu(instruction, context):
        match instruction:
            case 'play':
                playYTBMusic(context)

            case _:
                print("Command not found")
                waitingWakeUp()