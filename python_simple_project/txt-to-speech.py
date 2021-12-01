from gtts import gTTS
import os
#allows you os to interact your python program

myText = "Never give up. Do your best and let God does the rest."

#specified the language that you want to use
language = "en" #english

output = gTTS(text = myText, lang = language, slow = False)

#save the output as output.mp3
output.save("output.mp3")

#when the output has been saved, it will automatically playing the converted audio file
os.system("start output.mp3")