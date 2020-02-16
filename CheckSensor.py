import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
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
        print("SMH " + str((stop - start) * 17150));
    GPIO.cleanup()
    time.sleep(0.01)

#while(1 == 1):
 #   if(GPIO.input(ECHO) != 0):
  #      print("Seen")
#while(true):
 #   if(GPIO.input(ECHO) != 0):
  #      os.system("python main.py")
