# Find the factors of a number

num = int(input("Enter a number: "))
print("1")

for i in range(2,num+1):
    if(num%i == 0):
        print(i)
