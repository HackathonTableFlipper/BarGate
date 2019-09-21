import RPi.GPIO as GPIO
import time
import sys
import os.path

start = 0
end = 100
step = 1
input = str(sys.argv)

servo = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo,GPIO.OUT)

if os.path.exists("GateIsOpen.txt"):
	if not "open" in input:
		pos = 0
else:
	if not "close" in input:
		pos = 100

p=GPIO.PWM(servo,50) # 50hz frequency

p.start(pos) # starting duty cycle

def openGate():
	for x in range(start,end,step):
		p.ChangeDutyCycle(x/10.0)
		time.sleep(0.01)
	open("GateIsOpen.txt", "wx")
	print("Gate opened")

def closeGate():
	for x in range(end,start,-step):
		p.ChangeDutyCycle(x/10.0)
		time.sleep(0.01)
	os.remove("GateIsOpen.txt")
	print("Gate closed")

try:
	print("Script name: ", sys.argv[0])
	print("Number of Arguments: ", len(sys.argv))
	print("Argument/-s: ", str(sys.argv))

	if "open" in input:
		openGate()
	if "close" in input:
		closeGate()

except KeyboardInterrupt:
    GPIO.cleanup()
