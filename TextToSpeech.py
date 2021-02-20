from gtts import gTTS
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import playsound
import random
from io import BytesIO

# pygame.init()
#
# def say(text):
#     tts = gTTS(text=text, lang='en')
#     fp = BytesIO()
#     tts.write_to_fp(fp)
#     fp.seek(0)
#     pygame.mixer.pre_init(48300, -16, 2, 4096)
#     pygame.mixer.init()
#     pygame.mixer.music.load(fp)
#     pygame.mixer.music.play()
#     while pygame.mixer.music.get_busy():
#         pygame.time.Clock().tick(10)
#
# say("Hey Jai Swaminarayan")

# TODO you can remove pyaudio things like packages and all
def say(text):
    tts = gTTS(text=text, lang='en')
    r = random.randint(1, 10000000)
    audio_file = "audio-"+str(r)+".mp3"
    tts.save(audio_file)
    playsound.playsound(audio_file, True)
    os.remove(audio_file)


# say("Hey Jai Sri krishna and how are you now")
