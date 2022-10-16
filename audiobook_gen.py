# PDF to audio and audio file converter
import pyttsx3
from PyPDF2 import PdfReader
from pathlib import Path


def read_text(pdf):
    # initialising empty content string and reader object
    reader = PdfReader(pdf)
    content = ""

    for page in reader.pages:
        # extracting the text from the pdf
        text_ = page.extract_text()
        content = content + text_

    return content


def convert_to_mp3(content, filename):
    # a new engine is being created
    engine = pyttsx3.init()

    # changing the voice of the audio   
    
    voices = engine.getProperty("voices")
    if len(voices) == 0:
        print("Unable to find any convertable voice on your system.")
        quit(1)

    voice = voices[1] if len(voices) > 1 else voices[0]
    engine.setProperty("voice", voice.id)

    #changing volume
    volume = engine.getProperty('volume')
    print ("initial volume:  %s" %volume )  #print initial volume level
    engine.setProperty('volume', 1.0)


    # creating the audio(mp3) file of the pdf content
    engine.save_to_file(content, f"./{filename}.mp3")
    engine.runAndWait()


if __name__ == "__main__":
    try:
        path = Path(input("Enter the path to the pdf file: "))
        if not path.exists():
            print("The path to the file you gave is incorrect/doesn't exist.")
            quit(1)

        name = input(
            "What would you like to name your audiobook (exclude extensions): "
        ).strip()

        print("Reading file...")
        content = read_text(path)
        print("Converting to audio...")
        convert_to_mp3(content, name)
        print("Audiobook created.")

    except Exception as e:
        print(f"An error occured: {e}.")
