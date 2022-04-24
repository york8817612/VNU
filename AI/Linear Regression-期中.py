import numpy as np
from sklearn.linear_model import LinearRegression
X = np.array([[1], [2], [2], [4], [5]])
y = np.array([[-3.2], [-6.1], [-5.7], [-11.2], [-15.5]])

reg = LinearRegression().fit(X, y)
reg.score(X, y)

# 斜率
print("Q1.", reg.coef_)

# 截距
print("Q2.", reg.intercept_)

# 與第五個點誤差
print("Q3.", reg.score(X, y))

# 預測x=6
print("Q4.", reg.predict(np.array([[6]])))

# 預測x=-6
print("Q5.", reg.predict(np.array([[-6]])))
