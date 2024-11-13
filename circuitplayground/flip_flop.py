from adafruit_circuitplayground import cp

green = (0, 255, 0)

while True:
    if cp.switch:
        for i in range (5):
            cp.pixels[i] = (0, 0, 0)
        for i in range(5,10):
            cp.pixels[i] = green
        else:
                for i in range (5):
                    cp.pixels[i] = green
                for i in range (5, 10):
                    cp.pixels[i] = (0, 0, 0)
                
                cp.pixels.brightness = 0.02
                # not finished

                #change line 8 to (0, 255, 0)
                #change line 10 to (0, 0, 0)
                #change line 13 to (0, 0, 0)
                #change line 15 to (0, 255, 0)