# -*- coding: utf-8 -*-
import numpy as np

x  = [1,3,4,3.5,2]
x1 = [2,1,3,4,3.5]
y  = [1,1,2,5,4]
y1 = [4,1,1,2,5]

def area(x, y):
    return 0.5 * (np.dot(x1, y) - np.dot(x, y1))
print (str(area(x,y)) + " units squared")






"""x     = np.array([1,3,4,3.5,2])
y     = np.array([1,1,2,5,4])
i     = np.array([0,1,2,3,4])
z = .5*((x[i-1]*y)-(y[i-1]*x))

print z"""



