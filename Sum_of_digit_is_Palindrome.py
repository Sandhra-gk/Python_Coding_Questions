# Given a number N.Find if the digit sum(or sum of digits) of N is a Palindrome number or not.

a = input("enter number: ")
a_list = list(a)
sum=0

for i in a_list:
    sum += int(i)
reverse = "".join(reversed(str(sum)))
if(str(sum) == reverse):
    print("Yes")
else:
    print("No")
