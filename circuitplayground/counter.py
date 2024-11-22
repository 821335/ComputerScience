import time
from adafruit_circuitplayground import cp

number_pixels = 10

lit_pixels = 0

pixel_color = (0, 0, 255)

def update_pixels():
    for i in range(number_pixels):
        if i < lit_pixels:
            cp.pixels[i] = pixel_color
        else:
            cp.pixels[i] = (0, 0, 0)


while True:
    if cp.button_a:
        if lit_pixels < number_pixels:
            lit_pixels += 1
        time.sleep(0.2)

    if cp.button_b:
        if lit_pixels > 0:
            lit_pixels -= 1
        time.sleep(0.2)

    update_pixels()

    time.sleep(0.1)