// Given an unsorted array Arr of size N of positive integers. One number 'A' from set {1, 2,....,N} is missing and one number 'B' occurs twice in array. Find these two numbers.

n = int(input("Enter size of array: "))
arr = []
k = 0
l = 0
m = 0

for i in range(0,n):
    arr.append(int(input()))
    
for i in range(1,n+1):
    count = 0
    for j in range(0,n):
        if(arr[j] == i):
            count = count + 1
    if(count == 0):
        k = k + i 
    elif(count == 2):
        l = l + i 
    else:
        m = m + 1 
        
print(l,k)
