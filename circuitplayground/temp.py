from adafruit_circuitplayground import cp

cp.pixels.brightness = 0.01

while True:
    temp_c = cp.temperature
    temp_f = (temp_c * 9 / 5) + 32

    if temp_f < 78:
        cp.pixels.fill((0, 0, 0))
        cp.pixels[0] = (0,0,1)
    elif temp_f > 78:
        cp.pixels.fill((0, 0, 0))
        cp.pixels[0] = (0,0,1)
        cp.pixels[1] = (0,0,1)
    elif temp_f > 79:
        cp.pixels.fill((0, 0, 0))
        cp.pixels[0] = (0,0,1)
        cp.pixels[1] = (0,0,1)
        cp.pixels[2] = (0,0,1)
    elif temp_f > 80:
        cp.pixels.fill((0, 0, 0))
        cp.pixels[0] = (0,0,1)
        cp.pixels[1] = (0,0,1)
        cp.pixels[2] = (0,0,1)
        cp.pixels[3] = (1,1,0)
    elif temp_f > 81:
        cp.pixels.fill((0, 0, 0))
        cp.pixels[0] = (0,0,1)
        cp.pixels[1] = (0,0,1)
        cp.pixels[2] = (0,0,1)
        cp.pixels[3] = (1,1,0)
        cp.pixels[4] = (1,1,0)
    elif temp_f > 82:
        cp.pixels.fill((0, 0, 0))
        cp.pixels[0] = (0,0,1)
        cp.pixels[1] = (0,0,1)
        cp.pixels[2] = (0,0,1)
        cp.pixels[3] = (1,1,0)
        cp.pixels[4] = (1,1,0)
        cp.pixels[5] = (1,1,0)
    elif temp_f > 83:
        cp.pixels.fill((0, 0, 0))
        cp.pixels[0] = (0,0,1)
        cp.pixels[1] = (0,0,1)
        cp.pixels[2] = (0,0,1)
        cp.pixels[3] = (1,1,0)
        cp.pixels[4] = (1,1,0)
        cp.pixels[5] = (1,1,0)
        cp.pixels[6] = (1,1,0)
    elif temp_f > 84:
        cp.pixels.fill((0, 0, 0))
        cp.pixels[0] = (0,0,1)
        cp.pixels[1] = (0,0,1)
        cp.pixels[2] = (0,0,1)
        cp.pixels[3] = (1,1,0)
        cp.pixels[4] = (1,1,0)
        cp.pixels[5] = (1,1,0)
        cp.pixels[6] = (1,1,0)
        cp.pixels[7] = (1,0,0)
    elif temp_f > 85:
        cp.pixels.fill((0, 0, 0))
        cp.pixels[0] = (0,0,1)
        cp.pixels[1] = (0,0,1)
        cp.pixels[2] = (0,0,1)
        cp.pixels[3] = (1,1,0)
        cp.pixels[4] = (1,1,0)
        cp.pixels[5] = (1,1,0)
        cp.pixels[6] = (1,1,0)
        cp.pixels[7] = (1,0,0)
        cp.pixels[8] = (1,0,0)
    elif temp_f > 86:
        cp.pixels.fill((0, 0, 0))
        cp.pixels[0] = (0,0,1)
        cp.pixels[1] = (0,0,1)
        cp.pixels[2] = (0,0,1)
        cp.pixels[3] = (1,1,0)
        cp.pixels[4] = (1,1,0)
        cp.pixels[5] = (1,1,0)
        cp.pixels[6] = (1,1,0)
        cp.pixels[7] = (1,0,0)
        cp.pixels[8] = (1,0,0)
        cp.pixels[9] = (1,0,0)

