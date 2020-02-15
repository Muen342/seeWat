import sys
from gtts import gTTS
def main():
  print(sys.version)
  
def txt2speech(filename):
  file = open(filename, "r")
  tts = gTTS(file.read())
  tts.save('hello.mp3')


if __name__== "__main__":
  main()

txt2speech("demofile.txt")


