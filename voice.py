from textToSpeech import perform_tts

text = "Hello world"
voice = "random"
preset = "fast"
print("Performing TTS")
perform_tts(text, voice, preset)
print("Done")