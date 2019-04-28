# -*- coding: utf-8 -*-
"""
HW 1 Q2 part 2: Vector Notation
"""
import numpy as np

x = [ 1, 3, 4, 3.5, 2, 1]   
y = [ 1, 1, 2, 5, 4, 1 ]    
#coords(x, y) = [ (1,1), (3,1), (4,2), (3.5,5), (2,4)]

i  = np.arange(0, 5, 1, dtype = int)
i2 = i +1
print 'area vectorized:', (x[i]*y[i2] - y[i]*x[i2]).sum()
 

