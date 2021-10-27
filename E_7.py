n = int(input())
dict = []
cnt = [[0,'Kinh']]
name = []
for i in range(n):
    temp = list(map(str,input().split()))
    dict.append(temp)
    check = False
    for x in cnt:
        if temp[1] == x[1]:
            x[0] += 1
            check = True
    if not check:
        cnt.append([1,temp[1]])

for i in dict:
    if i[1] == max(cnt)[1]:
        print(i[0])
        