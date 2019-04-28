# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 16:44:56 2019

@author: lopez
"""

### Part B
"""
Area of Polygon usuing vecorization 
"""
import numpy as np 
X = [1, 3, 4, 3.5, 2]    #Xn components 
Y = [1, 1, 2, 5, 4]      #Yn components 
def PolyAreaVec( X,Y):   # Defining the area of Polygon 
    return 0.5*np.abs(np.dot(X,np.roll(Y,1))-np.dot(Y,np.roll(X,1)))
print('Area of Polygon_Vec', PolyAreaVec( X, Y))
