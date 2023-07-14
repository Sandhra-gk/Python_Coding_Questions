// Find the factorial of the given number

import math
num = int(input("Enter number: "))
fact = math.factorial(num)
print(fact)

OR

num = int(input("Enter number: "))
fact=1
for i in range(1,num+1):
    fact = fact*i
    
print(fact)
