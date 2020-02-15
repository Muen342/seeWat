import sys
from gtts import gTTS
import playsound
import os


def main():
  print(sys.version)
  
def txt2speech(filename):
  file = open(filename, "r")
  tts = gTTS(file.read())
  tts.save('hello.mp3')
  cwd = os.getcwd()
  print(cwd)

  playsound.playsound("hello.mp3", True)
  
  #p = vlc.MediaPlayer("file:///" + cwd + "hello.mp3")
  #p.play() 



if __name__== "__main__":
  main()

txt2speech("demofile.txt")


