import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model

# Input data

data = pd.read_csv('data_linear.csv')
X = np.array(data[['Diện tích']])
Y = np.array(data[['Giá']])

# print(data.info())

# print(X)
one = np.ones((X.shape[0], 1))
Xbar = np.concatenate((one, X), axis=1)

regr = linear_model.LinearRegression(fit_intercept=False)
regr.fit(Xbar, Y)

w_0 = regr.coef_[0][0]
w_1 = regr.coef_[0][1]
x0 = np.linspace(30, 100, 2)
y0 = w_0 + w_1*x0

plt.plot(X, Y, 'ro')
plt.plot(x0, y0)
plt.xlabel('Diện tích')
plt.ylabel('Giá')
plt.show()

