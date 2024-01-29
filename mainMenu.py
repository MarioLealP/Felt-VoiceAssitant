import sys
sys.path.append("extraRepos")
from speechRecognition import speechToText
from youtubePlayer import playMusic
from textToSpeech import speakToMe
import soundfile as sf


def mainOptions():
    
    speakToMe()



    #command = speechToText()
    #if command == "youtube" or command == "music":
        #playMusic()
    #else:
        #print("Command not recognized")