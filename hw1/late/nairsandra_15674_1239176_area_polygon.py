# -*- coding: utf-8 -*-
#anaconda2, Python 2.7
"""
- compute area of an irregular polygon.
variables:
    x_i = abscissa of vertex
    y_i = ordinate of vertex
    n = number of vertices

"""

#import numpy
#======================================
#       define variables
#======================================


n = 3
x_1 = 3
y_1 = 1
x_2=2
y_2=3
x_3=0
y_3=1
l_x=[x_1,x_2,x_3]
l_y=[y_1,y_2,y_3]

#======================================
#     compute savings
#======================================
def area(l_x, l_y, n):
    """
    :input
    
    parameters:
    l_x = x-coordinates of the vertices
    l_y = y-coordinates of the vertices 
    n = number of vertices
    :output
        area of an irregular polygon
    """
    x_s = 0
    y_s = 0        
#temporary variables x_s and y_s used to store values during computations
#using index i    
    for i in range(n-1):
        print(i)
        x_s = x_s + l_x[i]*l_y[i+1]
        y_s = y_s + l_y[i]*l_x[i+1]
#This takes care of formula except for the last summand, which we account by:-     
    x_s = x_s + l_x[n-1]*l_y[0]
    y_s = y_s + l_y[n-1]*l_x[0]
    print(x_s)
    print(y_s)
    
    A = 0.5*abs(x_s - y_s)
    return A

    
print(area(l_x, l_y, n))





