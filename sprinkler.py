import RPi.GPIO as GPIO

class Bot():

	def all(self):
		return [11,13,15]

	def __init__(self):
		GPIO.setmode(GPIO.BOARD)
		for switch in self.all():
			GPIO.setup(switch, GPIO.OUT)

	def turnOn(self, n):
		GPIO.cleanup()
		GPIO.setup(n, GPIO.OUT)
		GPIO.output(n, 1)

	def turnOff(self):
		GPIO.cleanup()