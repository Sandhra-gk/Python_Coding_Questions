# Given the first 2 terms A1 and A2 of an Arithmetic Series.Find the Nth term of the series. 

a1 = int(input("Enter 1st term: "))
a2 = int(input("Enter 2nd term: "))
n = int(input("Enter n: "))

d = a2 - a1
nth_term = a1 + (n-1)*d 

print(nth_term)
