from adafruit_circuitplayground import cp

cp.pixels.brightness = 0.02

while True:
    temp = cp.tempature * 9/5 + 32

    if temp < 60:
        cp.pixels[0] = (0, 0, 255)
    else:
        cp.pixels[0] = (0, 0, 0)

    if temp > 60:
        cp.pixels[1] = (28, 0, 227)
    else:
        cp.pixels[1] = (0, 0, 0)

    if temp > 64:
        cp.pixels[2] = (57, 0, 199)
    else:
        cp.pixels[2] = (0, 0, 0)

    if temp > 68:
        cp.pixels[3] = (85, 0, 170)
    else:
        cp.pixels[3] = (0, 0, 0)

    if temp > 72:
        cp.pixels[4] = (113, 0, 142)
    else:
        cp.pixels[4] = (0, 0, 0)

    if temp > 76:
        cp.pixels[5] = (142, 0, 113)
    else:
        cp.pixels[5] = (0, 0, 0)

    if temp > 80:
        cp.pixels[6] = (170, 0, 85)
    else:
        cp.pixels[6] = (0, 0, 0)
    
    if temp > 84:
        cp.pixels[7] = (199, 0, 57)
    else:
        cp.pixels[7] = (0, 0, 0)
    
    if temp > 88:
        cp.pixels[8] = (227, 0, 28)
    else:
        cp.pixels[8] = (0, 0, 0)

    if temp > 92:
        cp.pixels[9] = (255, 0, 0)
    else:
        cp.pixels[9] = (0, 0, 0)

    cp.pixels.show()