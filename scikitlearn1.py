# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 01:51:16 2017

@author: samdwise
"""
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm
digits = datasets.load_digits()
print(digits.data)
print(digits.target)
print(digits.images)
dif = svm.SVC(gamma=0.001, C=100)
print(len(digits.data))
x,y = digits.data[:-1], digits.target[:-1]
dif.fit(x,y)
print('Prediction:', dif.predict(digits.data[-1]))
plt.imshow(digits.images[-1],cmap=plt.cm.gray_r, interpolation="nearest")
plt.show()

