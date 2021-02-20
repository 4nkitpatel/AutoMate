import pyperclip
import TextToSpeech
import eel

# TODO remove clipboard package it was install
@eel.expose
def selectToSpeech(stop):
    pyperclip.copy("")
    while True:
        try:
            TextToSpeech.say(pyperclip.paste())
            pyperclip.copy("")
        except Exception as e:
            print(e)
            pass
        if stop():
            print("  Exiting loop.")
            break
