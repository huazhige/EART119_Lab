# -*- coding: utf-8 -*-
"""
HW 4 problem 4 part b
Benjamin Zhu 1696575
Pf. Tomas Goebel 
Astro/Earth 119

Finding the 3 equations using secant method
NOTE:
    I am using the exact same code as problem 2 while 
    changing some variables, so notations and everything 
    will almost the exactly the same
"""

#=======================================================
#           imports
#=======================================================

import numpy as np
import matplotlib.pyplot as plt
import opt_utils as utils
import os

#=======================================================
#           (a) f(x) = cos(x)**2 + 0.1
#                   from -10 to 10
#=======================================================

def ft2 (x):
    return np.cos(x)**2 + 0.1

#defining steps, starting points, and create
#an empty list for results to be stored
p       = 0
i       = 0
N       = 20
ini_x1  = -11
ini_x2  = -10
x_intcpt= []
x_intcpt.append(0.0001) #allows the while loop to pass the
                        #iterations

while i < N:
    #finding the roots using functions from opt_ utils
        root = utils.my_Secant(ft2, ini_x1, ini_x2)
        i       += 1
        ini_x1  += 1 #advancing from -10 to 10
        ini_x2  += 1
        #print ('attempts', i, ini_x1, ini_x2, root)
        if root == None:
            pass
        elif ft2 (root) < 0.001: #filter out results that aren't roots
            if (root-x_intcpt[p])/root < 0.01: #filter out repeated results
                pass
            else:
                p += 1    #adding the new result into the list 
                x_intcpt.append(root)    #and advance the list
                pass
        else:
            pass

x_intcpt.remove(0.0001) #removing this element since it
                        #has no more uses
if len(x_intcpt) == 0:
    print('there is no root')
else:
    print (x_intcpt)