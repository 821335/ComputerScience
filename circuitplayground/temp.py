from adafruit_circuitplayground import cp

cp.pixels.brightness = 0.02

while True:
    temp_c = cp.temperature
    temp_f = (temp_c * 9 / 5) + 32
    print(f"temperature:  {temp_f:.2f}    °f")
    
    for i in range(10):
        if i == 0 and temp_f < 78:
            cp.pixels[i] = (0, 0, 1)
        elif i == 1 and temp_f > 78:
            cp.pixels[i] = (0, 0, 1)
        elif i == 2 and temp_f > 79:
            cp.pixels[i] = (0, 0, 1)
        elif i in (3, 4, 5, 6) and temp_f > 80 + (i - 3):
            cp.pixels[i] = (1, 1, 0)
        elif i in (7, 8, 9) and temp_f > 84 + (i - 7):
            cp.pixels[i] = (1, 0, 0)
        else:
            cp.pixels[i] = (0, 0, 0)

        cp.pixels.show()