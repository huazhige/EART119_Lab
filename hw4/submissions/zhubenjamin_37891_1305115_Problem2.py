# -*- coding: utf-8 -*-
"""
HW 4 Porblem 2 
Benjamin Zhu 1696575
Pf. Tomas Goebel 
Astro/Earth 119

Find the intersection between f(t) and g(t) using the Secant method
"""

#=======================================================
#           imports
#=======================================================

import numpy as np
import matplotlib.pyplot as plt
import opt_utils as utils
import os

#=======================================================
#           functions and parameter definitions
#=======================================================
#defining fucntion f(t)
def f_t (t):
    c       = 1.1
    ini_t   = 2.5
    return c*(t - ini_t)**2
#defining function g(t)
def g_t (t):
    A       = 5
    ini_t   = 2.5
    return A*t +ini_t
#defining f(t)-g(t) as the function of h(t)
    #where roots of h(t) are interception points
def h_t (t):
    return f_t(t) - g_t(t)
    
#defining t for plotting
t       = np.arange(-10, 10, 0.5)

#=======================================================
#           Secant Method calculations
#=======================================================
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
    root = utils.my_Secant(h_t, ini_x1, ini_x2)
    i       += 1
    ini_x1  += 1 #advancing from -10 to 10
    ini_x2  += 1
    if h_t (root) < 0.001: #filter out results that aren't roots
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

#=======================================================
#           printing results for part a and b
#=======================================================

print ('there are', len(x_intcpt), 'x-intercepts')

result  = 0
count   = len(x_intcpt)
for i in range(count):          #printing out all the results
    print('t', x_intcpt[result],'f(t)', f_t(x_intcpt[result]),
          'g(t)', g_t(x_intcpt[result]))
    result += 1

#=======================================================
#           plotting for part c
#=======================================================
aX  = plt.subplot()
aX.plot(t, h_t(t))
aX.grid(True, which='both')
aX.axhline(y=0, color='k')
aX.axvline(x=0, color='k')

plt.xlabel( 't' )
plt.ylabel( 'f(t)-g(t)' )
os.chdir('prob2_partC_figure')
plt.savefig('part C graph.png')
plt.show ()