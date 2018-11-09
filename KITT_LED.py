import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

pins=[40,38,36,32,26,24,22,18,16,7,11,13,15,29,31,33]

GPIO.setup(pins,GPIO.OUT) 

for pin in pins:
    GPIO.setup(pin,GPIO.OUT)

while True:
    for num in range(len(pins)):
        if num >= 0:
            if num < 15:
                GPIO.output(pins[num],1)
                GPIO.output(pins[num+1],1)
                GPIO.output(pins[num-1],0)
            if num == 15:
                GPIO.output(pins[num-1],0)
                pins = list(reversed(pins))
        time.sleep(0.05)






# if num < num-1:




 #for x in range(len(pins)):
    #   if x >= 0 :
    #      GPIO.output(pins[x], 1)
