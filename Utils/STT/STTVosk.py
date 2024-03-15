from vosk import Model, KaldiRecognizer
import pyaudio

print("Loading model...")

model = Model(r"E:\Felt-VoiceAssitant\ExtraRepos\VoskModel")

recognizer = KaldiRecognizer(model, 16000) 

def speechToText():
    global model, recognizer
    mic = pyaudio.PyAudio()
    stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192) 
    stream.start_stream()
    print("Done")
    while True:
        data = stream.read(4096)
        if recognizer.AcceptWaveform(data):
            text = recognizer.Result()
            print(f"' {text[14:-3]} '")

speechToText()