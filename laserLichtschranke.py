import RPi.GPIO as GPIO
import os, time
import requests

RECEIVER_PIN = 24

URL = 'http://localhost:8080/graphql'
headers = {'content-type': 'application/json'}

def callback_blocked(channel):
    time.sleep(0.01)
    if GPIO.input(channel):
	requests.post(URL, data='{"query":"{blocked(blocked:true)}"}',headers=headers)
        print("Lichtschranke wurde unterbrochen")
        # alternativ kann ein Script / Shell Befehl gestartet werden
        # os.system("ls")
    else :
	requests.post(URL, data='{"query":"{blocked(blocked:false)}"}',headers=headers)
        print("offen")



if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(RECEIVER_PIN, GPIO.IN)
#    GPIO.add_event_detect(RECEIVER_PIN, GPIO.BOTH, callback=callback_blocked, bouncetime=200)
    print(GPIO.input(RECEIVER_PIN))

#
#    try:
#        while True:
#            time.sleep(1.0)
#            # print(GPIO.input(RECEIVER_PIN))
#
#    except:
#        # Event wieder entfernen mittels:
#        GPIO.remove_event_detect(RECEIVER_PIN)

