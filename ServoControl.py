import RPi.GPIO as GPIO                                                                                                                                                                                                                                                                                    start = 500                                                                                             end = 1000                                                                                              step = 1                                                                                                                                                                                                        servo = 22                                                                                                                                                                                                      GPIO.setmode(GPIO.BOARD)                                                                                GPIO.setup(servo,GPIO.OUT)                                                                              # in servo motor,                                                                                       # 1ms pulse for 0 degree (LEFT)                                                                         # 1.5ms pulse for 90 degree (MIDDLE)                                                                    # 2ms pulse for 180 degree (RIGHT)                                                                                                                                                                              # so for 50hz, one frequency is 20ms                                                                    # duty cycle for 0 degree = (1/20)*100 = 5%                                                             # duty cycle for 90 degree = (1.5/20)*100 = 7.5%                                                        # duty cycle for 180 degree = (2/20)*100 = 10%                                                                                                                                                                  p=GPIO.PWM(servo,50) # 50hz frequency                                                                                                                                                                           p.start(2.5) # starting duty cycle (it set the servo to 0 degree)                                                                                                                                               def openGate():                                                                                                 for x in range(start,end,step):                                                                                 p.ChangeDutyCycle(x/100.0)                                                                              time.sleep(0.01)                                                                                print "Gate opened"                                                                                                                                                                                     def closeGate():                                                                                                for x in range(end,start,-step):                                                                                p.ChangeDutyCycle(x/100.0)                                                                              time.sleep(0.01)                                                                                print "Gate closed"                                                                                                                                                                                      import RPi.GPIO as GPIO
import time

start = 500
end = 1000
step = 1

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

p=GPIO.PWM(servo,50) # 50hz frequency

p.start(2.5) # starting duty cycle (it set the servo to 0 degree)

def openGate():
	for x in range(start,end,step):
			p.ChangeDutyCycle(x/100.0)
			time.sleep(0.01)
	print "Gate opened"

def closeGate():
	for x in range(end,start,-step):
			p.ChangeDutyCycle(x/100.0)
			time.sleep(0.01)
	print "Gate closed"

try:
	while True:
			openGate()
			time.sleep(2)
			closeGate()
			time.sleep(2)

except KeyboardInterrupt:
    GPIO.cleanup()