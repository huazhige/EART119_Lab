# -*- coding: utf-8 -*-
#anaconda2, Python 2.7
"""
- compute area of an irregular polygon.
variables:
    l_x_i = abscissae of vertices
    l_y_i = ordinates of vertices
    

"""
import numpy as np
#======================================
#       define variables
#======================================

#for triangle:-

l_x_3=[3,2,0]
l_y_3=[1,3,1]

#for rectangle:-

l_x_4=[0,2,2,0]
l_y_4=[0,0,3,3]

#for pentagon:-

l_x_5=[1,3,4,3.5,2]
l_y_5=[1,1,2,5,4]

#======================================
#     compute area
#======================================
def area_vec(l_x, l_y):
    """
    :input
    
    parameters:
    l_x = x-coordinates of the vertices
    l_y = y-coordinates of the vertices 
    :output
        area of an irregular polygon
    """
   
   
    if len(l_x) != len(l_y):
       return "Error"
    #if the input vector is ill-defined, we need an error message   
    else:
       l_y_shift = np.concatenate((l_y[1:len(l_y)], l_y[0]), axis = None)
 #carry out dot product      
       x_p = np.dot(l_x, l_y_shift, out = None) 
       
       l_x_shift = np.concatenate((l_x[1:len(l_x)], l_x[0]), axis = None)
       y_p = np.dot(l_y, l_x_shift, out = None) 
        
       A = 0.5*(x_p-y_p)
        
       return A
    
print("Area of triangle A_3 =" + str(area_vec(l_x_3, l_y_3)))
print("Area of rectangle A_4 =" + str(area_vec(l_x_4, l_y_4)))   
print("Area of rectangle A_5 =" + str(area_vec(l_x_5, l_y_5)))   
  
       
#temporary variables x_p and y_p used to store values during computations
#using index i 

