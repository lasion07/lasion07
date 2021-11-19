from os import system, times

begin = 0

time = times()[1]
for i in range(100000000):
    begin += 1

print(times()[1] - time)