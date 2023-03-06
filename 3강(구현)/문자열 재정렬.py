target = input()

string = ""
number = 0

for n in target:
    if ord('0') <= ord(n) <= ord('9'):
        number += ord(n) - ord('0')
    else:
        string += n

s= sorted(list(string))
string = ''.join(s)

print(string + str(number))