# print the list of words whose count in a string is more than or equal to a particular count

string = input()
number = int(input())

string = string.split()
counts = dict()
for word in string:
    if word in counts:
        counts[word]+=1 
    else:
        counts[word]=1 

key_list = []

for key in counts:
    if counts[key] >= number:
        key_list.append(key)
        
if len(key_list)>0:
    print(key_list)
else:
    print("NA")
