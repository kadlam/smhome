import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

GPIO.cleanup()

class Bot():

	def __init__(self):
		self.GPIO = GPIO

	def turnOn(self, n):
		GPIO.cleanup()
		GPIO.output(n, 1)

	def off(self):
		GPIO.cleanup()