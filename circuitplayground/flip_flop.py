from adafruit_circuitplayground import cp

while True:
     if not cp.switch:
        for i in range (5):
            cp.pixels[i] = (0, 0, 0)
        for i in range(5,10):
            cp.pixels[i] = (0, 255, 0)
     else:
          for i in range (5):
              cp.pixels[i] = (0, 255, 0)
          for i in range (5, 10):
              cp.pixels[i] = (0, 0, 0)
          
          cp.pixels.brightness = 0.02