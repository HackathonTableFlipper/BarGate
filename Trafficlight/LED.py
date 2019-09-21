import RPi.GPIO as GPIO
import sys

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
RED = 23
GREEN = 18
BLUE = 25
GPIO.setup(RED,GPIO.OUT)
GPIO.output(RED,0)
GPIO.setup(GREEN,GPIO.OUT)
GPIO.output(GREEN,0)
GPIO.setup(BLUE,GPIO.OUT)
GPIO.output(BLUE,0)

if (len(sys.argv) > 1): 
  request = sys.argv[1]
  GPIO.output(RED,int(request[0]))
  GPIO.output(GREEN,int(request[1]))
  GPIO.output(BLUE,int(request[2]))

