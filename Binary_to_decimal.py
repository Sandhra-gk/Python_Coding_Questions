// Convert binary number to decimal number

binary = input("Enter binary number: ")
binary_list = list(binary)
length = len(binary_list)
sum=0

for i in range(0, length):
    power = length-i-1
    sum += int(binary_list[i])*pow(2,power)
    
print(sum)
    
