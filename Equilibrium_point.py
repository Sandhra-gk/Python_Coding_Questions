# Given an array A of n positive numbers. The task is to find the first Equilibrium Point in an array. 
# Equilibrium Point in an array is a position such that the sum of elements before it is equal to the sum of elements after it.

n = int(input("Enter size of array: "))
arr = []
sum1=0
sum2=0

for i in range(0,n):
    arr.append(int(input()))

if(n == 1):
    print("1")
else:
    j = n-1
    for i in range(0,n):
        sum1 = sum1 + arr[i]
        sum2 = sum2 + arr[j]
        if(sum1 == sum2):
            print(i+2)
            break
        else:
            j = j-1
    
