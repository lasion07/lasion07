A = {100,212,3330,101}
B = set()

def xd10(num):
    temp = num
    point = False
    while temp > 0:
        if temp % 10 == 0:
            point = True
        elif temp % 10 == 1:
            point = True
        temp = int(temp/10)

    return point

def ss10(num1, num2):
    pos1 = set()
    pos2 = set()
    def vt(num, pos):
        p = 0
        for i in str(num):
            if i == '0' or i == '1':
                pos.add(p+1)
            p += 1

    vt(num1, pos1)
    vt(num2, pos2)
    return pos1 == pos2

for i in A:
    if xd10(i):


        x = False
        for j in B:
            if ss10(i,j): x = True
        if not x:
            B.add(i)
print(B)


