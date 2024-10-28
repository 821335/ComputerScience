import random

r = random.randrange(0,10)
# 0 is inclusive and the 10 is Exclusive
# 0 <= result < 10
print(r)

p = random.random()
if p < .25:
    print("success")
else:
    print("fail")
