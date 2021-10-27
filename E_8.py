string = input()
if string.count('1')%2==0:
    n = string.count('1')/2
    temp = ''
    vt = -1
    for i in range(len(string)):
        if string[i] == '1':
            n-=1
        if not n:
            vt = i
    print(string[0:vt:1])
    print(string[vt:])
else: print('NO')
