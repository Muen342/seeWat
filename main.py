import sys
from gtts import gTTS
import playsound

def main():
  print(sys.version)
  txt2speech("demofile.txt")
  
def txt2speech(filename):
  file = open(filename, "r")
  tts = gTTS(file.read())
  tts.save('hello.mp3')
  playsound.playsound("hello.mp3", True)

if __name__== "__main__":
  main()




