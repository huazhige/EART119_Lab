# -*- coding: utf-8 -*-
"""
Spyder Editor
Homework 1 ASTR/EART 112
Rafael Nunez
#2.2
"""
import numpy as np
def area_polygon_vec(xList, yList):     #starts the definition of the area with x and y varying
    xArr = np.array(xList)              #turns the list of x into an array
    yArr = np.array(yList)              #turns the list of y into an array
    v1 = 0
    v2 = 0                              #gives v1 and v2 initial values to add to
    for i in range(len(xArr)):
        if i == len(xArr) - 1:
            y = yArr[0]
        else:
            y = yArr[i+1]
        v1 += xArr[i] * y
    for i in range(len(yArr)):
        if i == len(yArr) - 1:
            x = xArr[0]
        else:
            x = xArr[i+1]
        v2 += yArr[i] * x               #same idea as in area_polygon
    print "the area of A is ", 0.5 * (v1 - v2)
    
area_polygon_vec([1.0, 3, 4, 3.5, 2],[1.0, 1, 2, 5, 4])