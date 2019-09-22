import RPi.GPIO as GPIO
import time
import sys
import os.path

input = sys.argv

servo = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo,GPIO.OUT)

p=GPIO.PWM(servo,50) # 50hz frequency

if len(input)>1:
    print("given position:" + input[1])
    pos = int(input[1])
    if 0 <=  pos <= 100:
        p.start(pos)
    else:
        print("pls provide a value to the sript, that is ranged between 0 and 100")
    p.start(0)
    p.ChangeDutyCycle(pos)
    GPIO.cleanup()
else:
     print("pls provide a value to the sript, that is ranged between 0 and 100")
     GPIO.cleanup()

