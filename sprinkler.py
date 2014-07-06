import RPi.GPIO as GPIO

class Bot():

	def __init__(self):
		self.GPIO = GPIO
		self.GPIO.setmode(self.GPIO.BOARD)
		self.GPIO.cleanup()

	def turnOn(self, n):
		self.GPIO.cleanup()
		self.GPIO.setup(n, self.GPIO.OUT)
		self.GPIO.output(n, 1)

	def cleanup(self):
		self.GPIO.cleanup()