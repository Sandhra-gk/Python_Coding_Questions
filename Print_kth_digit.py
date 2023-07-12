# Given two numbers A and B, find Kth digit from right of AB.

a = int(input("Enter a: "))
b = int(input("Enter b: "))
k = int(input("Enter k: "))

a_pow_b = a**b  
final = str(a_pow_b)
length = len(final)
select = length-k

final_array = list(final)
print(final_array[select])
