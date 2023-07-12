# Given non-zero two integers N and M. The problem is to find the number closest to N and divisible by M. If there are more than one such number, then output the one having maximum absolute value.

n = int(input("Enter number: "))
m = int(input("Enter number closest to: "))
division = int(n/m) 
print(division)
modulus = int(n%m) 
print(modulus)
next_div_p = (m*division) + m
print(next_div_p)
next_div_n = (m*division) - m
print(next_div_n)

if(n>=0):
    if(modulus == 0 or modulus == 1):
        print(m*division)
    else:
        print(next_div_p)
else:
    if(modulus == 0 or modulus == 1):
        print(m*division)
    else:
        print(next_div_n)

