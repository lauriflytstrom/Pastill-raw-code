import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)


pins=[7,16,18,22,24,26,32,36,38,40,11,13,15,19,21,23]

for pin in pins:
    GPIO.setup(pin,GPIO.OUT)

while True:
    for pin in pins:
        GPIO.output(pin,0)
