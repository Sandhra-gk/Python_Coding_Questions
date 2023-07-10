#Given an array arr[] and an integer K where K is smaller than size of array, the task is to find the Kth smallest element in the given array. It is given that all array elements are distinct.

n = int(input("Enter size of array: "))
arr = []

for i in range(0,n):
    arr.append(int(input()))
    
k = int(input("Enter k: "))

arr.sort()

print(arr[k-1])
    
