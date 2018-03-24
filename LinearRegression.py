from sklearn import linear_model
reg = linear_model.LinearRegression()
X = [[0,0], [1,1], [2,2]]
y = [0,1,2]
reg.fit(X, y)
print(reg)
print(reg.coef_)
print(reg.intercept_)

test = [[5, 5]]
print(reg.predict(test))
print(reg.score(X, y))