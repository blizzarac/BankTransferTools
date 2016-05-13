from sklearn import tree

features=[[140, 1], [130, 1], [150, 2], [160, 2], [ 170,2], [100, 1], [120, 1], [200, 2]]
labels= [0, 0, 1, 1, 1, 0, 0, 1]

clf= tree.DecisionTreeClassifier()
clf= clf.fit(features, labels)

print clf.predict([100, 1])
