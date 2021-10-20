import math


x = float(input())
F = (pow(x,2)+math.exp(x)+math.sin(x)) / (math.sqrt(pow(x,2) + 1))
print('F(x)=',F)