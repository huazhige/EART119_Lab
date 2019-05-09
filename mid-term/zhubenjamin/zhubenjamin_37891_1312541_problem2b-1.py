# -*- coding: utf-8 -*-
"""

Finding roots for the following functions
f1(x) = x**5 + (2/5)*x**2 - 2
f2(x) = exp(-x/10) + x
f3(x) = 10*np.sin(x/4) + 0.1*(x+12)

"""
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import opt_utils as opt
import os

#============================================================
#               a
#============================================================
#defining functions
def f1 (x): 
    return np.exp(-x/10) + x

#setting parameters
xmin,xmax   = -10, 10
i           = -10 
N           = 1
root        = []
root.append(-20) #adding a number to kick start the loop
a           = 0
eps         = 1e-3

while i < xmax: #looping with -10 to 10 and test out multiple intervels
   #print (i, i+N)
   #print root
   curr_root = opt.my_Secant(f1, i, i+N, N=30)
   if f1(i+N)-f1(i) <= eps: #filter out secant lines that doesn't cross the x-axis
       pass
   elif curr_root == None:  #filter out results that doesn't work
       pass
   elif f1(curr_root) - f1(root[a]) < eps: #filter out similar results
       pass
   elif curr_root - root[a] > eps:  #adding correct results to the list
       root.append(opt.my_Secant(f1, i, i+N))
       a += 1    
   i += N

root.remove(-20) #remove the useless variable
a_root = np.asarray(root) #convert from list to array for calculation purpose
print ('the root is at:', a_root)

#plotting
x   = np.linspace(-10, 10, 100)
y   = np.linspace(-6, 6, 12)
ax = plt.subplot()
ax.plot(x, f1(x))
ax.plot(root, f1(a_root), 'ko', label = a_root)
ax.grid()
ax.legend()
ax.set_ylim([-6,6])

plt.savefig('problem 2b.png')














