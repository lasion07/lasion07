def Input():
    n = int(input())
    temp = list(map(int, input().split()))
    return temp

x = Input()

Cnt_list = dict()
def Count():
    for i in x:
        Cnt_list[i] = x.count(i)

Count()
def Output(x):
    for i in Cnt_list:
        print(i,':',Cnt_list[i])

Output(Cnt_list)