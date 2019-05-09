# -*- coding: utf-8 -*-
"""
Created on Wed May  8 08:26:25 2019

@author: colli
"""

import numpy as np
import matplotlib.pyplot as plt
import opt_utils
#==============================================================================
#Question 2
#==============================================================================

#===================================================================================
#                                params
#===================================================================================
xmin, xmax = -10, 10

x0    = 5
# root finding
tol = 1e-6

#range of function
t=np.linspace(xmin, xmax, 1000)
#==============================================================================
#Part a
#==============================================================================
def f1(x):
    return (x**5) + (2/5)*(x**2) - 2

####find root of fn########
root1=opt_utils.my_Secant( f1, x0, x0+10, N = 40)
print 'root of f1 is: ', root1

############plotting######
plt.figure(1)
plt.plot( t, f1( t),  'b-', label = 'f1(x)')
plt.plot( [root1], [f1(root1)],   'r*', mfc = 'w', ms = 10, label = ('Root: %.3f' %root1))
plt.plot( [xmin, xmax], [0,0], '--')
plt.grid(True)
plt.ylim( -10, 10)
plt.xlabel('x')
plt.ylabel('f1(x) value')
plt.title('f1(x)')
plt.legend(loc='upper left')
plt.savefig('Question_2_f1.png')




#==============================================================================
#Part b
#==============================================================================
def f2(x):
    return np.exp(-(x/10)) + x

####find root of fn########
root2=opt_utils.my_Secant( f2, x0, x0+10, N = 40)
print 'root of f2 is: ', root2

############plotting######
plt.figure(2)
plt.plot( t, f2( t),  'b-', label = 'f2(x)')
plt.plot( [root2], [f2(root2)],   'r*', mfc = 'w', ms = 10, label = ('Root: %.3f' %root2))
plt.plot( [xmin, xmax], [0,0], '--')
plt.grid(True)
plt.ylim( -10, 10)
plt.xlabel('x')
plt.ylabel('f2(x) value')
plt.title('f2(x)')
plt.legend(loc='upper left')
plt.savefig('Question_2_f2.png')



#==============================================================================
#Part c
#==============================================================================
def f3(x):
    return 10*np.sin(x/4) + 0.1*(x+12)

####find root of fn########
root3=opt_utils.my_Secant( f3, x0, x0+10, N = 40)
print 'root of f3 is: ', root3

############plotting######
plt.figure(3)
plt.plot( t, f3( t),  'b-', label = 'f3(x)')
plt.plot( [root3], [f3(root3)],   'r*', mfc = 'w', ms = 10, label = ('Root: %.3f' %root3))
plt.plot( [xmin, xmax], [0,0], '--')
plt.grid(True)
plt.ylim( -10, 15)
plt.xlabel('x')
plt.ylabel('f3(x) value')
plt.title('f3(x)')
plt.legend(loc='upper left')
plt.savefig('Question_2_f3.png')



