#python2.7
"""
HW 4 #4

    - find the roots of the following functions using the secant method

@author: scarletpasser
"""
import numpy as np
import opt_utils

################################# A ####################################

#function 1
def f_1(x):
    return -x**5 + (x**2)/3. + 0.5

#interval for guess between 1 and 10, derivative equals 0 at x = 0
root_1 = opt_utils.my_Secant(f_1, 1, 10, tol = 1e-4, N = 20)

print 'root 1: ', root_1

################################# B ####################################

#function 2
def f_2(x):
    return np.cos(x)**2 + 0.1

#this function never crosses the x - axis, secant methos returns infinity
root_2 = opt_utils.my_Secant(f_2, -10, 10, tol = 1e-4, N = 20)

print 'root 2: ', root_2

################################# C ####################################

#function 3
def f_3(x):
    return np.sin(x/3) + 0.1*(x+5)

root_3 = opt_utils.my_Secant(f_3, -3, 3, tol = 1e-4, N = 20)

print 'root 3: ', root_3
