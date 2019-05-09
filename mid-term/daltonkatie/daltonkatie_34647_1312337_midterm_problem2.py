# -*- coding: utf-8 -*-
"""
Created on Wed May  8 08:43:51 2019

@author: kardalto
"""

import numpy as np
import matplotlib.pyplot as plt
import opt_utils


#range for each function 
time = np.linspace(-10,10,1000)



#------------------------------------------------------------------------------
#       first function
#------------------------------------------------------------------------------
def f1_x(x):
    return(-x**5 + (2./5)*x**2 -2)
    
plt.figure(1)
plt.ylabel('Function')
plt.title('Roots of Three Functions')
plt.legend()
plt.subplot(221)
plt.plot(time, f1_x(time), 'ro', ms = 2)
plt.ylim(-2.1,1) #play with this range until the plot is precise
plt.xlim(-2,2)
plt.plot(-1.0882465935220864,0,'ko')
plt.xlabel('Time(s)')
plt.ylabel('Function')
plt.title('Roots of Three Functions')
plt.legend()
plt.show()

root1 = opt_utils.my_Secant(f1_x, -2.1,-1.9)
print('The root is: ',root1) 

#------------------------------------------------------------------------------
#       second function
#------------------------------------------------------------------------------
def f2_x(x):
    return (np.exp(-x/10.)+x)

plt.subplot(222)
plt.plot(time, f2_x(time), 'bo', ms = 2)
plt.ylim(-1.5,1.5)
plt.xlim(-2,2)
plt.plot(-1.1183078051936663,0,'ko')
plt.xlabel('Time(s)')
plt.show()

root2 = opt_utils.my_Secant(f2_x, -1,1)
print('The root is: ',root2) 

#------------------------------------------------------------------------------
#       third function
#------------------------------------------------------------------------------
def f3_x(x):
    return (np.sin(x/4)+(0.1*(x+12)))

plt.subplot(223)
plt.plot(time, f3_x(time), 'go', ms = 2)
plt.ylim(-4,4)
plt.xlim(-5,0)
plt.plot(-3.8268907657023092,0,'ko')
plt.ylabel('Function')
plt.xlabel('Time(s)')
plt.show()

root3 = opt_utils.my_Secant(f3_x, -2,2)
print('The root is: ',root3) 

