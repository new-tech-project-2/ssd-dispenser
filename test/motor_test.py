import RPi.GPIO as GPIO
import time


motorA1 = 4
motorA2 = 17

def MotorControl(num):
	if num:
		GPIO.output(motorA1, GPIO.HIGH)
		GPIO.output(motorA2, GPIO.LOW)
	else:
		GPIO.output(motorA1, GPIO.LOW)
		GPIO.output(motorA2, GPIO.HIGH)

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW)

MotorControl(1)
time.sleep(3)
MotorControl(0)
time.sleep(3)

GPIO.cleanup()
