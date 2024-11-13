import time
from adafruit_circuitplayground import cp

interval = 0.367

while True:
    cp.pixels.fill((0, 255, 0))
    time.sleep(interval)

    cp.pixels.fill((0, 0, 0))
    time.sleep(interval)

    cp.pixels.brightness = 0.03