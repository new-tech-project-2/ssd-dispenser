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
def stop():
	GPIO.setup(4, GPIO.OUT, initial=GPIO.LOW)
	GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW)

def init():
	GPIO.setmode(GPIO.BCM)
	
	GPIO.setup(4, GPIO.OUT, initial=GPIO.LOW)
	GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW)


def MotorControl(num):
	if num != 0:
		GPIO.output(motorA1, GPIO.HIGH)
		GPIO.output(motorA2, GPIO.LOW)
	elif num == 0:
		GPIO.output(motorA1, GPIO.LOW)
		GPIO.output(motorA2, GPIO.LOW)

def user_touch():
	MotorControl(0)
	data = pn532.read_mifare().get_data()
	print("data: ",data)
	sleep(0.5)
	res = ""
	for i in range(-7,0):
    		if i == -7 and int(data[i]) < 10:
        		res = "0"
    		res += str(hex(data[i]))[2:]
	print("user code: ", res)
	return res
	
	
	

def user_drink():

	MotorControl(1)
	sleep(1.5)
	MotorControl(0)

def get_token():
	return TOKEN

def clear():
	init()
	GPIO.cleanup()
	

if __name__ == "__main__":
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(4, GPIO.OUT, initial=GPIO.LOW)
	GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW)
	GPIO.output(motorA1, GPIO.LOW)
	GPIO.output(motorA2, GPIO.LOW)
	GPIO.cleanup()

