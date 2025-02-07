from ev3dev2.led import Leds
print("performing rainbow...")
leds = Leds()
while True:
    leds.animate_rainbow()
    input()