import math

n = int(input())
l = list(map(int,input().split()))

# kiem tra so nguyen to 3 nghiem
def kt(num) -> bool:
    for i in range(2,int(math.sqrt(num))+1,1):
        if num % i == 0:
            return True
    return False

cnt = 0
for i in l:
    if kt(i):
        cnt += 1

print(cnt)
