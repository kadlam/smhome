import RPi.GPIO as GPIO

class Bot():

	def all(self):
		return [11,13,15,19,21,23]

	def __init__(self):
		GPIO.setmode(GPIO.BOARD)
		for switch in self.all():
			GPIO.setup(switch, GPIO.OUT)

	def turnOff(self):
		for switch in self.all():
			GPIO.output(switch, 0)

	def turnOn(self, n):
		self.turnOff()
		GPIO.output(n, 1)

	def cleanup(self):
		GPIO.cleanup()
	
