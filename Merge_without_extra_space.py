# Given two sorted arrays arr1[] and arr2[] of sizes n and m in non-decreasing order. Merge them in sorted order without using any extra space. 
Modify arr1 so that it contains the first N elements and modify arr2 so that it contains the last M elements.

N = int(input("Enter size of array 1: "))
arr1 = []

for i in range(0, N):
    arr1.append(int(input()))
    
M = int(input("Enter size of array 2: "))
arr2 = []

for i in range(0, M):
    arr2.append(int(input()))
    
array = []
array = arr1 + arr2
array3 = sorted(array)

for i in range(0,N+M):
    print(array3[i])
    
    
