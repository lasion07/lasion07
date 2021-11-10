list_a = input().split()

new_a = []
L = []

for i,j in enumerate(list_a,0):
    if int(j) % 2 != 0:
        L.append(i)
    else:
        new_a.append(j)

[print(i) for i in L]
print(new_a)