# Get the starting and ending number from the user and then print all the prime numbers within the range.


start = int(input("Enter starting point: "))
end = int(input("Enter ending point: "))

for i in range(start, end+1):
    count=0
    for j in range(1,i):
        if(i%j == 0):
            count = count+1
    if(count == 1):
        print(i,"")
        
    
        
