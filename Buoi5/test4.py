import math

string, n = input().split()
n = int(n)

string_temp = string

for i in range(0,n):
    temp = ''
    cnt = 0
    for j in range(len(string_temp)):
        if j < len(string_temp)-1 and string_temp[j] == string_temp[j+1]:
            cnt += 1
        else:
            cnt += 1
            temp += str(cnt) + string_temp[j]
            cnt = 0
    print(temp)
    string_temp = temp

