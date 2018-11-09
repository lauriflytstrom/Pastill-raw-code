import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)     
GPIO.setup(13,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)

GPIO.output(7,0)   
GPIO.output(13,0)
GPIO.output(11,0)
GPIO.output(15,0)
