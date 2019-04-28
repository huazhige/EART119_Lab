# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 16:35:27 2019

@author: Nessa
"""

import numpy as np

# Test rectangle coordinates

Xi = [0, 2, 2, 0]
Yi = [0, 0, 3, 3]

# Test triangle2 coordinates
Xi_t = [3, 2, 0]
Yi_t = [1, 3, 1]

Xi_poly = [1, 3, 4, 3.5, 2]
Yi_poly = [1, 1, 2, 5, 4]

n = len(Xi)
n_t = len(Xi_t)
n_poly = len(Xi_poly)


def area_polygon (n, Xi, Yi):
    f1 = 0.0
    for i in range(n):
       f1 += ((Xi[i]*Yi[(i+1)%n]) - (Yi[i]*Xi[(i+1)%n]))
       #print (f1)
    f1 = abs(f1/2)
    if i == n-1:
        print (f1)
    
    
area_polygon (n, Xi, Yi)

area_polygon (n_t, Xi_t, Yi_t)

print ('POLYGON AREA =') 
area_polygon(n_poly, Xi_poly, Yi_poly)



