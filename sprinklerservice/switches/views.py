from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import View
from switches.models import Switch

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

bot = Bot()

def index(request):
    return HttpResponse("You're looking at Sprinklers")

def detail(request, switch_id):
    switch_id = int(switch_id)
    if switch_id > 0 and switch_id < 7:
        sprinkler = Switch.objects.get(id=switch_id)
        bot.turnOn(int(sprinkler.pinId))
        return HttpResponse("You're looking at Sprinkler %s." % switch_id)        
    else:
        bot.turnOff()
        return HttpResponse("You've entered an invalid number.")

def active(request, switch_id):
    switch_id = int(switch_id)
    if switch_id > 0 and switch_id < 7:
        sprinkler = Switch.objects.get(id=switch_id)
        bot.turnOn(int(sprinkler.pinId))
        return HttpResponse("Sprinkler %s is now active." % switch_id)
    else:
        bot.turnOff()
        return HttpResponse("You've entered an invalid number.")
