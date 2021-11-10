#B1

string_i = input()
index = int(input())

print(string_i[0:index:1]+string_i[len(string_i):index-1:-1])