# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 20:38:43 2017

@author: samdwise
"""

from sklearn.datasets import load_breast_cancer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
cancer = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(cancer_data, cancer.target, strafity=cancer.target, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, strafity=cancer.target, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, stratify=cancer.target, random_state=42)
knn = KNeighborsClassifier()
knn.fit(X_train,y_train)
print('Accuracy of knn n=5, on the training set', format(knn.score(X_train,y_train)))
print('Accuracy of test set: {:.3f}', format(knn.score(X_test, y_test)))
X_train,X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, stratify=cancer.target, random_state=66)
training_accuracy = []
test_accuracy = []
neighbors_settings = range(1,11)

for n_neighbors in  neighbors_settings:
    clf = KNeighborsClassifier(n_neighbors = n_neighbors)
    clf.fit(X_train,y_train)
    training_accuracy.append(clf.score(X_train,y_train))
    test_accuracy.append(clf.score(X_test,y_test))
    
plt.plot(neighbors_settings, training_accuracy, label='Accuracy of the training set')
plt.plt(neighbors_settings, test_accuracy, label='Accuracy of the test set')
plt.plot(neighbors_settings, test_accuracy, label='Accuracy of the test set')
plt.ylabel('Accuracy')
plt.xlabel('Number of neigbors')
plt.legend()
plt.show()
plt.plot(neighbors_settings, test_accuracy, label='Accuracy of the test set') 