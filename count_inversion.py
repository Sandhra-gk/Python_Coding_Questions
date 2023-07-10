Given an array of integers. Find the Inversion Count in the array. Two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.

n = int(input("enter size of array: "))
arr = []
count=0

for i in range(0,n):
    arr.append(int(input()))
    
for i in range(0,n):
    for j in range(i+1,n):
        if(arr[i]>arr[j]):
            count += 1 
            
print(count)
