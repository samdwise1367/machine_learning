from sklearn.datasets import load_iris
iris = load_iris()
frotype(iris)
print(iris.data)
print(iris.feature_names)
print(iris_target)
print(iris.target)
print
print(iris.target_names)
print(type(iris.data))
print(type(iris.target))
print(type(iris.target_names))
X = iris.data
print(iris.target.shape)
y = iris.target
print(X.shape)
print(y.shape)
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)
print(knn)
knn.fit(X,y)
knn.predict([3,5,4,2])
x_new = [[3,5,4,2],[5,4,3,2]]
knn.predict(x_new)
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X,y)
knn.predict(x_new)