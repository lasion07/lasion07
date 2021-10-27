string = input()

string_target = 'TRẺTRÂU'

cnt = 0
pos = 0
while pos < len(string):
    if string[pos] == string_target[cnt]:
        cnt += 1
        if cnt == len(string_target):
            break
    pos += 1

if cnt == len(string_target):
    print('TRẺ TRÂU')
else: print('Không TRẺ TRÂU')
