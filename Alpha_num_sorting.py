# Sort a string with alphabets followed by numbers

string = input()
alphabets = []
numbers = []

for ch in string:
    if ch.isalpha():
        alphabets.append(ch)
    else:
        numbers.append(ch)

final_array = sorted(alphabets)+sorted(numbers)
output = ''.join(final_array)
print(output)
