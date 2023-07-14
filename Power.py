# Get any number as the input from user for base and exponents, then calculate the power of the number.

import math

base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))

power = math.pow(base, exponent)
print(power)

OR

import math

base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))
power=1

for i in range(0, exponent):
    power = power*base
    
print(power)
