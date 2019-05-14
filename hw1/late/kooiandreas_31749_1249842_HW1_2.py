#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IDE: Spyder
Andreas Kooi
April 14, 2019

HW1.2
Consider a polygon with five vertices in Cartesian coordinates: 
    (1,1); (3,1); (4,2); (3.5, 5); (2,4)
The area can simply be computed from the know vertices using the following equation:
A = ½|(x1y2 + x2y3 + … xn-1yn + xny1) - (y1x2 + y2x3 + … + yn-1xn + ynx1)|

Your function will take two vectors (xi and yi) as input and return the area of the
polygon A. 
Write to different functions: 1) area_polygon.py – which solves the
above equation within a for loop and 2) area_polyon_vec.py – which solve the equation
using vector notation.
"""

#=============================
#       import nessecary modules
#============================

import numpy as np




#=============================
#       Functions
#============================

def area_poly( x_vec, y_vec ):
    
    i = 0
    i2 = 0
    term1 = 0
    term2 = 0
    
    for val in x_vec:
        if val == x_vec[-1]:
            term1 += val*y_vec[0]
        else:
            term1 += val*y_vec[i + 1]
            i += 1
    for val in y_vec:
        if val == y_vec[-1]:
            term2 += val*x_vec[0]
        else:
            term2 += val*x_vec[i2 + 1]
            i2 += 1
    
    area = 0.5*np.abs((term1 - term2))
    
    return(area)
    


def area_polyon_vec( x_vec, y_vec ):
    
    y_new = np.transpose( np.append(y_vec[1:len(y_vec)], y_vec[0]))
    x_new = np.transpose( np.append(x_vec[1:len(x_vec)], x_vec[0]))
        
    area = 0.5*np.abs((np.dot(x_vec,y_new) - np.dot(y_vec,x_new)))
    
    return(area)
    
    
    

#=============================
#       Parameters
#=============================
    
xvals = np.array([1, 3, 4, 3.5, 2])
yvals = np.array([1, 1, 2, 5, 4])





#=============================
#       Computations
#=============================

area1 = area_poly(xvals,yvals)
area2 = area_polyon_vec(xvals,yvals)

print('The area using area_polygon is %.2f and the area using area_polyon_vec is %.2f'%(area1, area2))