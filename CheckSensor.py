import RPi.GPIO as GPIO
import time

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
while(true):
    if(GPIO.input(ECHO) != 0):
        os.system("python main.py")
