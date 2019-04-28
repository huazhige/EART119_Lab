# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 11:46:34 2019

@author: eric_
"""
import numpy as np
#taking inputs for x-vector
x = input('Enter in elements for x vector with each element separated by a comma e.g. 2, 4, 6: ') 
xlist = x.split(", ")
x_vector = np.array(list(map(float, xlist))) #changing elements to floats


#taking inputs for y-vector
y = input('Enter in elements for corresponding y vector with each element separated by a comma: ')
ylist = y.split(", ")
y_vector = np.array(list(map(float, ylist))) #changing y elements to floats



x1 = np.roll(x_vector, -1) #roll command moves each index by -1 
y1 = np.roll(y_vector, -1)
print("x-vector = ", x_vector)
print("y-vector = ", y_vector)
print("x1 = : ", x1)
print("y1 = : ", y1)
total_area = (0.5)*(np.dot(x_vector, y1) - np.dot(y_vector, x1)) #area of irregular polygon
print(total_area)