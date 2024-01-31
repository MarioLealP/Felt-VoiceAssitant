import multiprocessing
import os
import subprocess
import settings
import sys
import playsound
from TTS.TTS.api import TTS
import time


def textToSpeech(text):
    filePath = "tempFiles/audio/tts.wav"
    tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC")
    tts.tts_to_file(text=text, file_path=filePath)
    print(filePath)
    playsound.playsound(filePath, True)
    os.remove(filePath)
    print(filePath)

    return()