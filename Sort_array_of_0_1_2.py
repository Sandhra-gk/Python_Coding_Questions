# Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.

n = int(input("Enter size of array: "))
arr = []

for i in range(0,n):
    arr.append(int(input()))
    
print(arr)
    
arr.sort()
print(arr)
