import time
import random
from adafruit_circuitplayground import cp

cp.pixels.brightness = 0.01

def turn_off_pixels():
    cp.pixels.fill((0, 0, 0))

def light_pixels(number_pixels):
    number_pixels = min(number_pixels, len(cp.pixels))
    for i in range(number_pixels):
        cp.pixels[i] = (0, 255, 0)

while True:
    if cp.button_a:

        number = random.randint(1, 10)
        light_pixels(number)
        time.sleep(0.5)
    if cp.button_b:
        turn_off_pixels()
        time.sleep(0.5)