s = input()

maxlen = 0

for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        temp_str = s[i: j]
        if s.find(temp_str,i+1,len(s)) != -1:
            maxlen = max(maxlen, len(temp_str))

print(maxlen)
