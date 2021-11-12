import math

n = int(input())
l = list(map(int,input().split()))

# tong cac uoc
def sumofdivisor(num):
    sum = 0
    for i in range(1,int(num/2)+1,1):
        if num % i == 0:
            sum += i
    return sum

c = []

for i in l:
    if sumofdivisor(i) > i:
        c.append(i)

print(len(c))
for i in c:
    print(i,end=" ")
