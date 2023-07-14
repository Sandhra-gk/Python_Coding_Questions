# Get a number as input from user and then check whether that number is a strong number or not.
# A number is said to be strong number if the sum of the factorial of each digit in the number is same as that of the number.

import math

num = int(input("Enter number: "))
str_num = str(num)
length = len(str_num)
sum=0

for i in range(0, length):
    fact = math.factorial(int(str_num[i]))
    sum = sum + fact
    
if(sum == num):
    print("It is a strong number");
else:
    print("It is not a strong number");
