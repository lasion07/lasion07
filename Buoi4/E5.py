def INPUT():
    l = list(map(int, input().split()))
    n = int(input())
    return l,n

l = []
n = 0
l,n = INPUT()

def RemoveFirstXNumber(l,x):
    for i in range(len(l)):
        if l[i] == x:
            l.pop(i)
            print(i)
            break
def RemoveAllXNumber(l,x):
    while x in l:
        l.remove(x)

def InsertY(l,x):
    def check(y):
        if y >= 0 and y <= len(l):
            return True
        return False
    y = int(input())
    while not check(y):
        y = int(input())
    l.insert(y,x)
    
print(l)
RemoveFirstXNumber(l,n)
print(l)
RemoveAllXNumber(l,n)
print(l)
InsertY(l,n)
print(l)

