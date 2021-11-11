string = input()
x = string[10:int(string.index(',')):]
y = string[int(string.index(','))+1:len(string)-1:]
print(x,y)