import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from scipy.special import expit

np.random.seed(2)

data = pd.read_csv("data_Logistic.csv")

X = np.array(data['Age']).reshape(len(data['Age']), 1)
y = np.array(data['Purchased'])

clf = linear_model.LogisticRegression(C=1e5).fit(X, y)
print('Accuracy =', clf.score(X, y))

X0 = y0 = X1 = y1 = np.array([])

for i in range(len(X)):
    if y[i] == 0:
        X0 = np.append(X0, X[i])
        y0 = np.append(y0, 0)
    else:
        X1 = np.append(X1, X[i])
        y1 = np.append(y1, 1)

plt.plot(X0, y0, 'ro', markersize=6)
plt.plot(X1, y1, 'bs', markersize=6)

X_test = np.linspace(18, 60, 1000)
threshold = -clf.intercept_/clf.coef_

loss = expit(X_test * clf.coef_ + clf.intercept_).ravel()
plt.plot(X_test, loss, color="green", linewidth=3)

plt.axis([18-1, 60+1, -1, 2])
plt.plot(threshold, .5, 'y^', markersize=8)
plt.title('Purchased rate by age')
plt.xlabel('Age')
plt.ylabel('Purchased (1) / Not Purchased (0)')
plt.show()
