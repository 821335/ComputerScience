from adafruit_circuitplayground import cp
import time
import random
cp.pixels.brightness= 0.02

shake_threshold = 15.0

colors_updated = False

while True:
    x, y, z = cp.acceleration

    if abs(x) > shake_threshold or abs(y) > shake_threshold or abs(z) > shake_threshold:
        if not colors_updated:
            for i in range(10):
                cp.pixels[i] = (
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0,255)
                )

            colors_updated = True

        time.sleep(0.1)

    else:
        colors_updated = False
