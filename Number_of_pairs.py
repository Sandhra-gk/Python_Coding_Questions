Given two arrays X and Y of positive integers, find the number of pairs such that xy > yx (raised to power of) where x is an element from X and y is an element from Y.

n = int(input("Enter size of array 1: "))
arr1 = []

m = int(input("Enter size of array 2: "))
arr2 = []

count=0

for i in range(0,n):
    arr1.append(int(input()))
    
for j in range(0,m):
    arr2.append(int(input()))
    for i in range(0,n):
        if((arr1[i]**arr2[j]) > (arr2[j]**arr1[i])):
            count += 1

print(count) 
