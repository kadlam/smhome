import RPi.GPIO as GPIO

class Bot():

	def __init__(self):
		self.GPIO = GPIO
		self.GPIO.setmode(self.GPIO.BOARD)

		self.GPIO.setup(11, self.GPIO.OUT)
		self.GPIO.setup(13, self.GPIO.OUT)

	def turnOn(self, n):
		self.GPIO.cleanup()
		self.GPIO.output(n, 1)

	def turnOff(self, n):
		self.GPIO.output(n, 0)

	def off(self):
		self.GPIO.cleanup()