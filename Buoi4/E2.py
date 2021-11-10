#B2

a = input()
L = ''
if len(a) < 2:
    print(L)
else:
    L = a[0] + a[1] + a[len(a)-2] + a[len(a)-1]
    print(L)