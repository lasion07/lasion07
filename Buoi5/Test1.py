a,b = input().split()

cnt = 0
i = 0

while i < len(b):
    temp = b.find(a,i)
    if temp != -1:
        cnt += 1
        i = temp
    i += 1

print(cnt)