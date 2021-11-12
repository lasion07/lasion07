import math

n = int(input())
l = list(map(int,input().split()))

# kiem tra so nguyen to 3 nghiem
def kt(num) -> bool:
    cnt = 0
    for i in range(2,int(num/2)+1,1):
        if num % i == 0:
            cnt += 1
    return (cnt==1)

cnt = 0
for i in l:
    if kt(i):
        cnt += 1

print(cnt)
