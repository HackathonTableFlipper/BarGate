import RPi.GPIO as GPIO
import time
import sys
import os.path

start = 500
end = 1000
step = 1
input = str(sys.argv)
isGateOpen = open("IsGateOpen.txt", "w+")

servo = 22

GPIO.setmode(GPIO.BOARD)
GPIO.setup(servo,GPIO.OUT)

# in servo motor,
# 1ms pulse for 0 degree (LEFT)
# 1.5ms pulse for 90 degree (MIDDLE)
# 2ms pulse for 180 degree (RIGHT)

# so for 50hz, one frequency is 20ms
# duty cycle for 0 degree = (1/20)*100 = 5%
# duty cycle for 90 degree = (1.5/20)*100 = 7.5%
# duty cycle for 180 degree = (2/20)*100 = 10%

pos = 100

try:
	if not os.path.exists('IsGateOpen.txt'):
		isGateOpn.write("false")
	else:
		isGateOpen.read()
	if isGateOpen == "false":
		pos = 1000
	if isGateOpen == "true":
		pos = 500
except KeyboardInterrupt:
		GPIO.cleanup()

p=GPIO.PWM(servo,50) # 50hz frequency

p.start(pos) # starting duty cycle (it set the servo to 0 degree)

def openGate():
	for x in range(start,end,step):
		p.ChangeDutyCycle(x/100.0)
		time.sleep(0.01)
	isGateOpen.write("true")
	print("Gate opened")

def closeGate():
	for x in range(end,start,-step):
		p.ChangeDutyCycle(x/100.0)
		time.sleep(0.01)
	isGateOpen.write("false")
	print("Gate closed")

try:
	print("Script name: ", sys.argv[0])
	print("Number of Arguments: ", len(sys.argv))
	print("Argument/-s: ", str(sys.argv))

	if "open" in input:
		openGate()
	if "close" in input:
		closeGate()

#try:
#       while True:
#		openGate()
#		time.sleep(2)
#		closeGate()
#		time.sleep(2)

except KeyboardInterrupt:
    GPIO.cleanup()
