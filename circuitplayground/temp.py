from adafruit_circuitplayground import cp

cp.pixels.brightness = 0.02

temp_numbers = [78, 79, 80, 81, 82, 83, 84, 85, 86]

colors = [
    (0, 0, 1),
    (0, 0, 1),
    (0, 0, 1),
    (1, 1, 0),
    (1, 1, 0),
    (1, 1, 0),
    (1, 1, 0),
    (1, 0, 0),
    (1, 0, 0),
    (1, 0, 0),
]


while True:
    temp_c = cp.temperature
    temp_f = (temp_c * 9 / 5) + 32
    print(f"temperature:  {temp_f:.2f}    °f") 

    for i in range(10):
        if i == 0:
            if temp_f < 78:
                cp.pixels[i] = colors[i]
            else:
                cp.pixels[i] = (0, 0, 0)
        elif temp_f > temp_numbers[i - 1]:
            cp.pixels[i] = colors[i]
        else:
            cp.pixels[i] = (0, 0, 0)