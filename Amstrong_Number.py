# For a given 3 digit number, find whether it is armstrong number or not. An Armstrong number of three digits is an integer such that the sum of the cubes of its digits is equal to the number itself. Return "Yes" if it is a armstrong number else return "No".

n = input("Enter number: ")
sum=0

for i in range(0,len(n)):
    num = int(n[i])
    sum = sum + (num**3)
    
if(sum == int(n)):
    print("Yes")
else:
    print("No")
