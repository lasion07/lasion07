aList = list(map(int, input().split()))

result = []

result.append(aList[0])

for i in range(1,len(aList)):
    result.append(result[i-1]+aList[i])

print(result)