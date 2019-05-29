# -*- coding: utf-8 -*-
#python 3.6
import numpy as np
import matplotlib.pyplot as plt

## Function definition ######
def fct_f(t):
    return 3*t**2*np.exp(t**3)

def fct_F(t):
    return np.exp(t**3)

#Integration fct##
def trapezoidal(fct_x, x0, xn, N):
    '''
    compostie trapezoidal method, implementation of eq. 3.17 pg 60 in Linga and Langtangen
    Params:
        fct_x  - comp. integral of the fct
        x0, xn - integration bounds
        N      - number of trapezoids
    Return:
        value of definite integral of fct_x
        between x0 and xn
    '''
    dx = float(xn - x0)/N
    #write sum as for loop
    f_Integ = 0.5*(fct_x(x0) + fct_x(xn))
    for i in range (1, N):
        f_Integ = fct_x(x0 + i*dx)
    #write sum in vectorized form
    #f_Integ = 0.5*(fct_x(x0) + fct_x(xn)) + (fct_x(x0 + dx*np.array(1, N, 1))).sum()
    return dx*f_Integ

## Parameters #########
xmin, xmax = 0, 1
N          = 10

## Num integration and plotting
#exact solution
f_IntExact = fct_F(xmax) - fct_F(xmin)

#numerical approx
f_IntNum = trapezoidal(fct_f, xmin, xmax, N)

#compare exact and numerical
print('Exact int: ', f_IntExact)
print('Numerical approx Trapezoidal: ', f_IntNum)

for curr_n in range(10, 1000, 200):
    f_IntNum = trapezoidal(fct_f, xmin, xmax, curr_n)
    print('increment dx' , float(xmax - xmin))
    print('Exact int: ', f_IntExact)
    print('Numerical approx: ', f_IntNum)
    
########################### Parameters ###########################
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

f_intNum = midpoint(fct_f, xmin, xmax, N)
print('Numerical approx Midpoint: ', f_intNum)
for curr_n in range(10, 1000, 200):
    f_intNum = trapezoidal(fct_f, xmin, xmax, curr_n)
    print('increment dx' , float(xmax - xmin))
    print('Numerical approx Midpoint: ', f_intNum)