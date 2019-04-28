# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

x = [1,3,4,3.5,2]
y = [1,1,2,5,4]

"""
xi = x[0]*y[1] + x[1]*y[2] + x[2]*y[3] + x[3]*y[4] + x[4]*y[0]


yi = y[0]*x[1] + y[1]*x[2] + y[2]*x[3] + y[3]*x[4] + y[4]*x[0]
    
def Area( xi, yi):
    return 0.5*abs(xi - yi)

print Area( xi, yi)
"""
for ix in x:
    xi = ix*y[x.index(ix)]
print xi
