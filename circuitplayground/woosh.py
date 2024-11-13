import time
from adafruit_circuitplayground import cp

interval = 0.1

while True:
    if cp.button_a:
        for i in range (10):
            cp.pixels[i] = (0, 0, 255)
            time.sleep(interval)
            cp.pixels[i] = (0, 0, 0)
            time.sleep(interval)
            cp.pixels.brightness = 0.03