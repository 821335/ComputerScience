# Amazon free shipping eligibilty
# prime customers OR purchases of over $25
# under 18, you need parent consent to purchase

def free_shipping(age, prime, cost, consent):
    if (prime == True or cost >= 25) and (age >= 18 or consent == True):
        print("free shipping applied")
    else:
        print("ineligible for free shipping...")


p = False
cos = 100
a = 12
con = True

free_shipping(p, cos, a, con)