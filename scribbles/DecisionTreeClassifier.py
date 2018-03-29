from sklearn import tree
from sklearn import metrics
X = [[0,0], [1,1]]
Y = [0,1]

Z = [[2,2]]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)
print(clf.predict(Z))

print(metrics.accuracy_score([1],clf.predict(Z)))

