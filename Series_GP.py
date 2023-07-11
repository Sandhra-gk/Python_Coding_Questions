# Given the A and R i,e first term and common ratio of a GP series. Find the Nth term of the series.

a = int(input("Enter 1st term: "))
r = int(input("Enter 2nd term: "))
n = int(input("Enter n: "))

d = pow(r,n-1)
nth_term = a*d

print(nth_term)
