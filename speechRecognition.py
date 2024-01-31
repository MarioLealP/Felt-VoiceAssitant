import speech_recognition as sr
from pocketsphinx import LiveSpeech

def speechToText():
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            print(command)
            return command
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""
    
def speechToTextSphinx():
    print("Listening...")
    for phrase in LiveSpeech():
        print(phrase)
        return phrase