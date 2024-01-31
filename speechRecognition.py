import speech_recognition as sr

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
    