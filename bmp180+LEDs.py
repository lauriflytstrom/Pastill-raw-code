import Adafruit_BMP.BMP085 as BMP085
sensor = BMP085.BMP085()

import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)     
GPIO.setup(13,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)

while True:
    i=(sensor.read_temperature())
    if i>=10.00: 
        GPIO.output(7,1) 
    if i>=15.00:
        GPIO.output(13,1)
    if i>=20.00:
        GPIO.output(11,1)
    if i>=25.00:
        GPIO.output(15,1)
    time.sleep(1)      
    GPIO.output(7,0)   
    GPIO.output(13,0)
    GPIO.output(11,0)
    GPIO.output(15,0)
    print ('Temp = {0:0.2f} *C'.format(sensor.read_temperature()))    

