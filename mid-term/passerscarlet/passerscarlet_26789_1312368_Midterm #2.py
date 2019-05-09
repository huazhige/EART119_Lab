#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
MIDTERM QUESTION 2

@author: scarletpasser
"""
import matplotlib.pyplot as plt
import numpy as np
import opt_utils as opt_utils

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                               params 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# -10 < x < 10 for all functions
x = np.arange( -10, 11)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                            function 1
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#function 1
def f_1(x):
    return x**5 + (2*x**2)/5 - 2

#using my secant method, derivative = 0 at 0 so x0 > 0
root1 = opt_utils.my_Secant(f_1, 1, 2) 

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                            function 2
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def f_2(x):
    return np.exp(-x/10) + x

#using my secant method, function is pretty well behaves so bounds matter less
root2 = opt_utils.my_Secant(f_2, -2, 5) 


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                            function 3
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def f_3(x):
    return 10*np.sin(x/4) + 0.1*( x+ 12)

#using my secant method
root3 = opt_utils.my_Secant(f_3, -5, 5) 


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                              plots 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

plt.title('problem 2: functions')

plt.subplot(311)  #plot function 1
plt.ylim(-10, 10) #y limit
plt.plot(x, f_1(x))
plt.plot(root1, 0, marker = 'o', label = 'root1 = 1.088')
plt.legend() #legend 

plt.ylabel('funciton 1')

plt.subplot(312) #plot function 2
plt.ylim(-10, 10) #y limit
plt.plot(x, f_2(x))
plt.plot(root2, 0, marker = 'o', label = 'root2 = -1.118')
plt.legend() #legend 

plt.ylabel('function 2')

plt.subplot(313) #plot function 3
plt.ylim(-10, 10) #y limit
plt.plot(x, f_3(x))
plt.plot(root3, 0, marker = 'o', label = 'root3 = -0.463')
plt.legend() #legend 

plt.xlabel('x')
plt.ylabel('function 3')
plt.savefig('Midterm #2 graph')
plt.show()