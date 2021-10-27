strinput = input()

even = []
odd = []
for i in strinput:
    if i >= '0' and i <= '9':
        if int(i)%2==0:
            even.append(i)
        else:
            odd.append(i)
kq = []
for i in even:
    kq.append(i)
for o in odd:
    kq.append(o)
print(kq)