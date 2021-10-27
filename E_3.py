strinput = ''

while True:
    strinput = input()
    print(len(strinput))
    if len(strinput) >= 10:
        break
print(strinput[2:7:1])

b = input()

lower_list = []
upper_list = []

for i in range(len(b)):
    if b[i] >= 'A' and b[i] <= 'Z':
        upper_list.append(b[i])
    if b[i] >= 'a' and b[i] <= 'z':
        temp = b[i]
        if temp == 'b':
            temp = 'g'
        lower_list.append(temp)

print(upper_list)
print(lower_list)

string = 'hElLo-mY-NAMe-iS-SuZIe'
new_string = ''
space = True

for i in range(len(string)):
    if string[i] >= 'A' and string[i] <= 'Z' :
        if space:
            new_string += string[i]
            space = False
        else:
            new_string += string[i].lower()
    elif string[i] >= 'a' and string[i] <= 'z':
        if space:
            new_string += string[i].upper()
            space = False
        else:
            new_string += string[i]
    else:
        new_string += ' '
        space = True

print(new_string)