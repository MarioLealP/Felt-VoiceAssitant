import sys
sys.path.append("extraRepos")
from speechRecognition import speechToText
from youtubePlayer.youtubePlayer import playMusic
from textToSpeech import speakToMe
from settings import Name
from commands import commands

def waitingWakeUp():
    wakeUpCall = speechToText()

    if(wakeUpCall.find(Name) == -1):
        waitingWakeUp()
    
    instruction = listenCommand(wakeUpCall)

    attemptsAtListening = 0
    
    #Checks if instruction was found if not attempts to listen 3 times before going back to sleep
    while(instruction == "Not Found"):
        attemptsAtListening += 1
        phrase = speechToText()
        listenCommand(phrase)
        if(attemptsAtListening == 3):
            waitingWakeUp()

    #instruction found goes to the menu to execute it
    instructionMenu(instruction)



def listenCommand(phrase):

    instruction = ""

    words = phrase.split()

    for word in words:
        for key in commands.keys():
            if word in commands.get(key):
                instruction = key
                return instruction #returns the instruction based on the command key

    return "Not Found"



def instructionMenu(instruction):
        match instruction:
            case 'play':
                playMusic()

            case _:
                print("Command not found")
                waitingWakeUp()