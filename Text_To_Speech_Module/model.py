from gtts import gTTS

import os

fh = open("AI_model_input.txt", "r")

myText = fh.read().replace("\n"," ")

language = 'en'

output = gTTS(text = myText, lang = language, slow = False)

output.save("output_voice.mp3")
fh.close()
os.system("start output_voice.mp3")