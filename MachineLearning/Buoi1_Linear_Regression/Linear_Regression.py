import math
import numpy as np
import matplotlib.pyplot as plt

# Tinh dao ham cua ham so
def derivative(x):
    return 2*x + 5*math.cos(x)
# Tinh gia tri ham so
def f(x):
    return x*x + 5*math.sin(x)

def gd(eta, x0):
    x = x0
    for _ in range(100):
        temp = x - eta*derivative(x)
        if abs(derivative(x)) < 1e-3:
            break
        x = temp
    return x

# Tinh gia tri nho nhat cua ham so

x_target = gd(.1, -5)

# Hien thi hinh ve

x = np.arange(-6,6,.1)

plt.plot(x, list(map(f,x)))

plt.annotate(f'~ {round(f(x_target),2)}', (x_target, f(x_target)), (x_target, f(x_target)+8), arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad=-0.1', color='r'))
plt.title('F(x) = x^2 + 5sin(x)')
plt.show()
