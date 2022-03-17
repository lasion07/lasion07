from __future__ import division, print_function, unicode_literals
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

np.random.seed(2)

data = pd.read_csv("data_Logistic.csv")

X = np.array([data['Age']])
y = np.array(data['Purchased'])

# extended data
X = np.concatenate((np.ones((1, X.shape[1])), X), axis=0)


def sigmoid(s):
    return 1 / (1 + np.exp(-s))


def logistic_sigmoid_regression(X, y, w_init, eta, tol=1e-4, max_count=100000):
    w = [w_init]
    N = X.shape[1]
    d = X.shape[0]
    count = 0
    check_w_after = 20
    while count < max_count:
        # mix data
        mix_id = np.random.permutation(N)
        for i in mix_id:
            xi = X[:, i].reshape(d, 1)
            yi = y[i]
            zi = sigmoid(np.dot(w[-1].T, xi))
            w_new = w[-1] + eta * (yi - zi) * xi
            count += 1
            # stopping criteria
            if count % check_w_after == 0:
                if np.linalg.norm(w_new - w[-check_w_after]) < tol:
                    return w
            if count % 1000 == 0:
                epoch_time = int(time.time())
                print('w = {}, Time: {}'.format(w[-1], epoch_time))
            w.append(w_new)
    return w


eta = .05
d = X.shape[0]
w_init = np.random.randn(d, 1)

w = logistic_sigmoid_regression(X, y, w_init, eta)
print(w[-1])

X0 = X[1, np.where(y == 0)][0]
y0 = y[np.where(y == 0)]
X1 = X[1, np.where(y == 1)][0]
y1 = y[np.where(y == 1)]

plt.plot(X0, y0, 'ro', markersize=8)
plt.plot(X1, y1, 'bs', markersize=8)

start = min(X[1])
end = max(X[1])

xx = np.linspace(start, end, 1000)
w0 = w[-1][0][0]
w1 = w[-1][1][0]
threshold = -w0 / w1
yy = sigmoid(w0 + w1 * xx)
plt.axis([start-1, end+1, -1, 2])
plt.plot(xx, yy, 'g-', linewidth=2)
plt.plot(threshold, .5, 'y^', markersize=8)
plt.title('Purchased rate by age')
plt.xlabel('Age')
plt.ylabel('Purchased (1) / Not Purchased (0)')
plt.show()
