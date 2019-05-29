# -*- coding: utf-8 -*-
"""
Created on Fri May 17 15:39:10 2019

@author: bruno
"""

import numpy as np
from scipy import integrate


#Defines the function sin(x)
def fx(x):
    return np.sin(x)

#Defines the function 2xe^x^2
def fx1(x):
    return 2 * x * np.exp(x**2)

def midpoint( fct_x, x0, xn, N):
    """
            Composite Midpoint method, eq. 3.21 page 66 in Linge & Langtangen
    :param fct_x:  - function whose integral is in question
    :param x1:     - integration bounds
    :param x2:     - integration bounds
    :param N:      - number of trapezoids, chose high number for high accuracy
    :return:   - integral of fct_x between x0 and xn
    """
    dx     = float( xn-x0)/N
    a_xi   = x0 + 0.5*dx + np.arange( N)*dx
    f_int  = dx*( fct_x(a_xi)).sum()
    return f_int

'''
Similar to the midpoint method, this method basically just adds up all of the
little boxes created from the dx variable. It takes from the left side and
from the right side and it adds them all together.
'''
def ReimanSum( fct_x, x0, xn, N = 1000):
    """
            Composite Midpoint method, eq. 3.21 page 66 in Linge & Langtangen
    :param fct_x:  - function whose integral is in question
    :param x1:     - integration bounds
    :param x2:     - integration bounds
    :param N:      - number of trapezoids, chose high number for high accuracy
    :return:   - integral of fct_x between x0 and xn
    """
    dx   = float( xn-x0)/N
    left = x0 + dx + np.arange(0,N/2) * dx #Finds the left side half of the graph
    right = x0 + dx + np.arange(N/2,N) * dx #Finds the right side of the graph
    #Adds the two together so that the area under the curve is returned.
    f_int = (dx*( fct_x(right)).sum()) + (dx*( fct_x(left)).sum()) 
    return f_int

#The exact answer for the first fucntion
x_ans, err = integrate.quad(fx, 0, np.pi)
#The exact answer for the second function
x_ans_1, err1 = integrate.quad(fx1, 0 , 1)

print ("Using the Reiman sum the integral of fx is %1.5f") % ReimanSum(fx,0,np.pi)
print("Using the midpoint method the integral of fx is %1.5f") % midpoint(fx,0,np.pi,1000)
print ("The exact integral of fx is %1.1f" ) % x_ans
print("All of the methods produce the same answer")

print ("Using the Reiman sum the integral of fx1 is %1.5f") % ReimanSum(fx1,0,1)
print("Using the midpoint method the integral of fx1 is %1.5f") % midpoint(fx1,0,1,1000)
print ("The exact integral of fx1 is %1.5f" ) % x_ans_1
print("The midpoint method gives a better approximation in this case")



