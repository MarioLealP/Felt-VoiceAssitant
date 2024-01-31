import multiprocessing
import os
import subprocess
import settings
import sys
from pydub import AudioSegment
from pydub.playback import play
from TTS.api import TTS
import time


def textToSpeech(text):
    filePath = "tempFiles/audio/tts.wav"
    tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC")
    tts.tts_to_file(text=text, file_path=filePath)
    try:
        sound = AudioSegment.from_file(filePath, format="wav")
        play(sound)
    except:
        print("Error playing file")
    finally:
        
        os.remove(filePath)

    return()