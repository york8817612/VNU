from sklearn import tree
# 參數
X = [[0, 0], [1, 1], [1, 2], [1.9, 1], [1.9, 2], [1.8, 3], [1.8, 4], [2, 3], [2, 4], [3, 3], [2.1, 1], [2.2, 1.8], [3, 1.8], [3.5, 2], [4, 1.9]]
# 分屬0或1
Y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

# 預測(2, 1)
print("Q6.", clf.predict([[2., 1.]]))

# 預測(2.1, 1)
print("Q7.", clf.predict([[2.1, 1.]]))

# 預測(3, 3)
print("Q8.", clf.predict([[3., 3.]]))

# 預測(5, 1)
print("Q9.", clf.predict([[5., 1.]]))

# 預測(5, 3)
print("Q10.", clf.predict([[5., 3.]]))
