import SmartSound
import RPi.GPIO as GPIO
import time


newSound = SmartSound.SmartSound()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)

state = 0

while True:

        env = newSound.get_envelope()
        print env
        if(env > 150):
                if(state == 0):
                        print "on"
                        GPIO.output(21,GPIO.HIGH)
                        state = 1
                elif(state == 1):
                        print "off"
                        GPIO.output(21,GPIO.LOW)
                        state = 0


        time.sleep(0.5)
