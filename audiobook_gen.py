#PDF to audio and audio file converter
from importlib.resources import path
import pyttsx3
from PyPDF2 import PdfReader

path = input("Enter the full path of the pdf file: ")
reader = PdfReader(path)

#a new engine is being created
engine = pyttsx3.init()

#changing the voice of the audio
voices = engine.getProperty('voices')
voice = voices[1]
engine.setProperty('voice', voice.id)

#initialising empty content string
content = ""

#queuing the commands to speak the pages
for page in reader.pages:
    #extracting the text from the pdf
    text_ = page.extract_text()
    content =  content+text_
    engine.say(text_)

print(content)
#creating the audio(mp3) file of the pdf content
engine.save_to_file(content, "myaudio.mp3")  

print("mp3 file created!") 
#reading the text
engine.runAndWait()
print("Reading completed!")











