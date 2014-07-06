import RPi.GPIO as GPIO

class Bot():

	def __init__(self):
		GPIO.setmode(GPIO.BOARD)

	def turnOn(self, n):
		GPIO.cleanup()
		GPIO.setup(n, GPIO.OUT)
		GPIO.output(n, 1)

	def turnOff(self):
		GPIO.cleanup()