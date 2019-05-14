# -*- coding: utf-8 -*-

"""
compute the area of an irregular polygon with the use of vector notation
"""
import numpy as np

# test rectangle w area 6
l_x_rc = [0, 2, 2, 0]
l_y_rc = [0, 0, 3, 3]

#test triangle w area 3
l_x_tr = [3, 2, 0]
l_y_tr = [1, 3, 1]

#test pentagon
#(1,1); (3,1); (4,2); (3.5, 5); (2,4).
l_x_pen = [1,3,4,3.5,2]
l_y_pen = [1,1,2,5,4]

def area_polygon_vec(l_x, l_y):
    """
    - computes the area of polygon with vertices defined by 
    position vectors l_x and l_y
    
    :input
    l_x = the x-coordinates of the vertices
    l_y = the y-coordinates of the vertices in the same order as l_x
    
    :output
    A = the area of the polygon
    """
    x_N = len(l_x)
    y_N = len(l_y)
    
    if x_N != y_N:
        return -1
    else:
        l_y_shift = np.concatenate((l_y[1:y_N], l_y[0]),axis=None)
        x_sum = np.dot(l_x,l_y_shift, out=None) #elementwise multiplicaction
        
        l_x_shift = np.concatenate((l_x[1:x_N],l_x[0]),axis=None)
        y_sum = np.dot(l_y,l_x_shift, out=None)
        
        A = 0.5*abs(x_sum-y_sum)
        
        return A
    
print('test triangle, A=', area_polygon_vec(l_x_tr, l_y_tr))
print('test rectangle, A=', area_polygon_vec(l_x_rc, l_y_rc))
print('test pentagon, A=', area_polygon_vec(l_x_pen, l_y_pen))