import RPi.GPIO as GPIO

RECEIVER_PIN = 27

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(RECEIVER_PIN, GPIO.IN)
    print(GPIO.input(RECEIVER_PIN))

