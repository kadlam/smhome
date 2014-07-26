#18-JUL-2014 KGA: this version of ledtest modified for python3
#added paren to print function
from time import sleep
import sprinkler
bot = sprinkler.Bot()
tsec = 5

def turn_on_leds(pin):
    i = 0
    while i < 6:
        bot.turnOn(pin[i])
        print (pin[i])        
        sleep (1)
        i = i + 1
while True:
    turn_on_leds([11,13,15,19,21,23])
    bot.turnOff()
    print ("pause", tsec,"seconds")
    sleep (tsec)
    


