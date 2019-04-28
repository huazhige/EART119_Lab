# -*- coding: utf-8 -*-

import numpy as np

def AreaCircle(r):
     return  np.pi*r**2
 
def ApproxArea(r, a):
    a_Circle = AreaCircle(r)
    print(a_Circle)
    b = 0
    while  (a*b < a_Circle):
       b += 1
    b -= 1
    return b


r = 12.6
a = 1.5
print( ApproxArea( r, a))
 