# -*- coding: utf-8 -*-
"""
Created on Thurs May  15 22:15:34 2019

@author: Brendan Chapman
"""
#========================================================================================================================
" Extra Credit Homework"
""" Numerical Integration"""
#========================================================================================================================


#========================================================================================================================
"Question 1"
#========================================================================================================================
"a."

'Packages'

import os
import integration
import numpy as np
from math import e


'Variables'

def f(x):  return 3*(x**2)*(e**(x**3))

'Function'

"Midpoint"
a = integration.integMid(0,1,f,400 )

print(a)
"Trapezoidal"
b = integration.integTrap(0,1,f, 400)

print(b)

#========================================================================================================================
"Question 2"
#========================================================================================================================
"a."
"Variables"
count = 0 

"Function"
def g(x): return np.sin(x) 

"Mean Calculation"
xmin, xmax = 0,np.pi
array = np.arange(0,np.pi,1/1000,dtype=float)
for x in array:
    if x < 1000:
        g (x)
        x +=1
        sum
print(np.mean(array))
        

        
#print(np.mean(array))
        
"Integral"
c = integration.integTrap(0,np.pi, g, 1000)
print(c)
"b."
"Function"

def h(x): return 2*x*(e**(x**2))

"Mean Calculation"
xmin, xmax = 0,1
array1 = np.arange(0,1,1/1000,dtype=float)
for x in array1:
    if x < 1000:
        g (x)
        x +=1
        sum
print(np.mean(array1))
#print(np.mean(array1))
"Integral"

d = integration.integTrap(0,1, h, 1000)
print(d)

#========================================================================================================================
"Question 3"
#========================================================================================================================
"a."
"Function"
#f3(x,y) = ((x**2 + y**2)**(1/2))

#monte = integration.monteCarlo(f3)
"b."
"Function"
#w(x,y) = (x*(y**2))

'Packages'
'Variables'
'Function'


