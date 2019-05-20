# -*- coding: utf-8 -*-
#python2.7


# =============================================================================
#                              Problem 4.
# =============================================================================

import numpy as np
import opt_utils as opt

# =============================================================================
#                           Define functions
# =============================================================================

def f_1 ( x):
    """
    The function f_1 given in problem 4 of homework 4
    """
    
    Ans = -x**5 + (1/3)*x**2 + (1/2)
    
    return float(Ans)

def f_2 ( x):
    """
    The function f_2 given in problem 4 of homework 4
    """
    
    Ans = (np.cos(x))**2 + 0.1
    
    return float(Ans)

def f_3 ( x):
    """
    The function f_3 given in problem 4 of homework 4
    """
    
    Ans = np.sin((x/3)) + 0.1*(x + 5)
    
    return float(Ans)

# =============================================================================
#                           Define variables
# =============================================================================

x1 = np.arange(-10., 11., 1.)

# print(x1) # Unit testing

import numpy as np

x2 = np.arange(-3., 4., 1.)

# print(x2) # Unit testing

f1_root = opt.my_Secant(f_1, x1, x1+10.)
f2_root = opt.my_Secant(f_2, x1, x1+10.)
f3_root = opt.my_Secant(f_3, x2, x2+10.)

for i in np.arange(0,21,1):
    if f1_root == x1[i]:
        print 'The roots of f1 are ', f1_root
    if f2_root == x1[i]:
        print 'The roots of f2 are ', f2_root
    if i < 20:
        i += 1
    else:
        break
    
for i in np.arange(0,8,1):
    if f3_root == x2[i]:
        print 'The roots of f3 are ', f3_root
    if i < 8:
        i += 1
    else:
        break