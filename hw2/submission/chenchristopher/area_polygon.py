# -*- coding: utf-8 -*-
#python 2.7
"""
Computes the area of a polygon given its vertices
Input: array of x-values x, array of y-values y
Output: Area
"""

def area(x, y):
    sum = 0
    for i in range(x.size):
        sum = sum + 0.5 * (x[i - 1] * y[i] - y[i - 1] * x[i])
    return sum