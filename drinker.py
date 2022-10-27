import RPi.GPIO as GPIO
import time
from config import TOKEN
from py532lib.i2c import *
from py532lib.frame import *
from py532lib.constants import *
pn532 = Pn532_i2c()
pn532.SAMconfigure()


motorA1 = 4
motorA2 = 17


GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW)

GPIO.output(motorA1, GPIO.LOW)
GPIO.output(motorA2, GPIO.LOW)

def MotorControl(num):
	if num:
		GPIO.output(motorA1, GPIO.HIGH)
		GPIO.output(motorA2, GPIO.LOW)
	else:
		GPIO.output(motorA1, GPIO.LOW)
		GPIO.output(motorA2, GPIO.LOW)

def user_register():
        d = pn532.read_mifare().get_data()
	d = d[1:d.find(':')]
        print(d)
	return d
	
	

def user_drink():
	d = pn532.read_mifare().get_data()
	d = d[1:d.find(':')]

	print(d)
	sleep(1)
	MotorControl(1)
	sleep(3)
	MotorControl(0)

def get_token():
	return TOKEN

def clear():
	GPIO.cleanup()
	


