string = input()

list_number = []
new_string = ''
for i in range(len(string)):
    if string[i] == '+':
        new_string += ' '
    else:
        new_string += string[i]

list_number = [int(i) for i in new_string.split()]

list_number.sort()

for i,j in enumerate(list_number):
    if i != len(list_number) -1:
        print(j,end='+')
    else: print(j)