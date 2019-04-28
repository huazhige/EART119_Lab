# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 22:37:49 2019

Area of an Irregular Polygon
"""
import numpy as np

#==========================================================
#                      parameters
#==========================================================

X = [1, 3, 4, 3.5, 2, 1] # XY coordinates of all 5 vertices
Y = [1, 1, 2, 5,   4, 1] # 6th value a repeat of the first
Area = 0

#==========================================================
#                      Compute with for loop
#==========================================================

for i in np.arange( 0, 6):
    
    Area += (X[i]+X[i-1])*(Y[i-1]-Y[i])
    
print 'the area of the polygon is' ,0.5*abs(Area)


#==========================================================
#                      Compute with Vector Notation
#==========================================================

i = np.arange(0, 6)
    
print (X[i]+X[i-1])*(Y[i-1]-Y[i]) #I don't know what a scalar array is. I give up :( 