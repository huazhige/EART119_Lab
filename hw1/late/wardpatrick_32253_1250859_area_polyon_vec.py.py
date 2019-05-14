# -*- coding: utf-8 -*-

"""
Q2 part 2
"""
import numpy as np

xi = np.array([1,  3, 4, 3.5,  2])
yi = np.array([1,  1, 2, 5  ,  4])

i = np.arange(5)

t1 = (xi[0:4]*yi[1:5]).sum() + xi[-1]*yi[0]
t2 = (yi[0:4]*xi[1:5]).sum() + yi[-1]*xi[0]

A = .5*abs(t1-t2)
print ('Area:', A)