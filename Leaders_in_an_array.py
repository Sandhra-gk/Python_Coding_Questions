# Given an array A of positive integers. Your task is to find the leaders in the array. An element of array is leader if it is greater than or equal to all the elements to its right side. The rightmost element is always a leader. 

n = int(input("Enter size of array: "))
arr = []

for i in range(0,n):
    arr.append(int(input()))

for i in range(0,n):
    count=0
    for j in range(i+1, n):
        if(arr[i] > arr[j]):
            count += 1 
    if(count == n-i-1):
        print(arr[i])
    
