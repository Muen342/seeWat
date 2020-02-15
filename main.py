import sys
from gtts import gTTS
import playsound
import os, io
from tkinter import filedialog, Tk
from google.cloud import vision
from google.cloud .vision import types

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'ServiceAccountToken.json'

FileName = "testimg.jpg"
FolderPath = os.getcwd()
FullPath = os.path.join(FolderPath,FileName)

def GetText(FilePath):
	client = vision.ImageAnnotatorClient()


	with io.open(FilePath,'rb') as image:

		content = image.read()

	image = vision.types.Image(content=content)
	response = client.document_text_detection(image=image)
	return (response.full_text_annotation.text)


  
def txt2speech(filename):
  file = open(filename, "r")
  tts = gTTS(file.read())
  tts.save('hello.mp3')
  playsound.playsound("hello.mp3", True)

def main():
  print(sys.version)
  
  f = open("demofile.txt", "a")
  f.write(GetText(FullPath))
  f.close()
  
  txt2speech("demofile.txt")

if __name__== "__main__":
  main()




