from gpiozero import Button, LED
from time import sleep
import random

led = LED(17)

player_1 = Button(2)
player_2 = Button(3)

time = random.uniform(5, 10)
sleep(time)
led.on()

while True:
    if player_1.is_pressed:
        print("Player 1 is God!")
        break
    if player_2.is_pressed:
        print("Player 2 deserves a cake!")
        break

led.off()