# -*- coding: utf-8 -*-

"""
compute the area of an irregular polygon with the use of for loops
"""
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

def area_polygon(l_x, l_y):
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
        x_sum = 0
        y_sum = 0
        for i in range(x_N-1):
            x_sum += l_x[i]*l_y[i+1]
            y_sum += l_y[i]*l_x[i+1]
        x_sum += l_x[-1]*l_y[0]
        y_sum += l_y[-1]*l_x[0]
        
        A = 0.5*(x_sum-y_sum)
        
        if A >= 0:
            return A
        else:
            return -A
        
print('test triangle', area_polygon(l_x_tr, l_y_tr))
print('test rectangle', area_polygon(l_x_rc, l_y_rc))
print('test pentagon', area_polygon(l_x_pen, l_y_pen))