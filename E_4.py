n = int(input())

while n > 9:
    sum = 0
    temp = n
    while temp > 0:
        sum += temp%10
        temp=int(temp/10)
    n = sum

print(n)