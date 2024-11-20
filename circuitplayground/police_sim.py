import time
from adafruit_circuitplayground import cp

interval = 0.5
color_toggle = True
tone_toggle = True
cp.pixels.brightness = 0.02

while True:
    if color_toggle:
        cp.pixels.fill((255, 0, 0))
    else:
        cp.pixels.fill((0, 0, 255))
    color_toggle = not color_toggle

    if tone_toggle:
        cp.start_tone(500)
    else:
        cp.start_tone(900)
    tone_toggle = not tone_toggle

    time.sleep(interval)
    cp.stop_tone()