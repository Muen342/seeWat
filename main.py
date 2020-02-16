import sys
from gtts import gTTS
import playsound
import os, io
import RPi.GPIO as GPIO
import time
#from tkinter import filedialog, Tk
from google.cloud import vision
from google.cloud .vision import types
GPIO.setwarnings(False)
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'ServiceAccountToken.json'

FileName = "READPIC.jpg"
FolderPath = os.getcwd()
FullPath = os.path.join(FolderPath,FileName)

def GetText(FilePath):
    client = vision.ImageAnnotatorClient()


    with io.open(FilePath,'rb') as image:

        content = image.read()

    image = vision.types.Image(content=content)
    response = client.document_text_detection(image=image)
    if(response.full_text_annotation.text == ""):
       return "no text found"
    
    return (response.full_text_annotation.text)


  
def txt2speech(filename):
  file = open(filename, "r")
  text = file.read()
  #rawtext = raw(text)
  tts = gTTS(text)
  tts.save('hello.mp3')
  os.system("ffplay -nodisp -autoexit hello.mp3")

def camScan():
  print(sys.version)
  os.system("raspistill -o READPIC.jpg")
  f = open("demofile.txt", "w")
  f.write(GetText(FullPath))
  f.close()
  
  txt2speech("demofile.txt")

def main():
    while(1 == 1):
        GPIO.setmode(GPIO.BOARD)

        TRIG = 7
        ECHO = 12

        GPIO.setup(TRIG,GPIO.OUT)
        GPIO.output(TRIG,0)

        GPIO.setup(ECHO,GPIO.IN)
        time.sleep(0.1)

        GPIO.output(TRIG,1)
        time.sleep(0.0001)
        GPIO.output(TRIG,0)

        while GPIO.input(ECHO) == 0:
            pass
        start = time.time()

        while GPIO.input(ECHO) == 1:
            pass
        stop = time.time()
        #print((stop - start) * 17150)
        if(((stop - start) * 17150) < 10):
            camScan()
            
        GPIO.cleanup()
        time.sleep(0.01)

if __name__== "__main__":
  main()




