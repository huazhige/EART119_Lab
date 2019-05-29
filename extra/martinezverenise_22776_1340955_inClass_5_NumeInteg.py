# -*- coding: utf-8 -*-

"""
- We will be doing numerical integration of given function using midtpoint and trapizoidal methods
- ex: f(t)= 3t**2exp(t^3)
- F(t) = exp(t^3)
   - between: a, b 
   - with F'(t)= f(t)

"""
import numpy as np 
################################ fUNCTION DEF ##################################

###############################################################################
def fct_f(x):
    return 3*x**2*np.exp(x**3)
def fct_F(x):
    return np.exp(x**3)
## integration trap
def trapizoidal( fct_x, x0, xn, N):
    """
        composite trap method, reimplementation of ep 3.17 pg 60
        in Linge and Langtangen 
    Params: 
        fct_x - comp. integral of this fct. 
        x0, xn - integration bounds 
        N - number of trapizoids 
    Return:
        Value of definite integral of function btwn x0 and xn 
    """
    dx = float(xn - x0)/ N
    #write sum of for loop
    f_Integ = 0.5*(fct_x(x0) + fct_x(xn))
    for i in range (1, N):
        f_Integ = fct_x(x0 +i*dx)
        ## write sum  in vectorized form 
        #f_Integ = .5*(fct_x(x0)+ fct_x(xn))+(fct_x(x0+dx*np.arrange(1,N,1))).sum()
    return dx*f_Integ
print(trapizoidal)
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
print(midpoint)
########################### Parameters ########################################
xmin, xmax = 0, 1 
N = 10 
###############################################################################
#exact soultion 
f_IntExact = fct_F(xmax) - fct_F(xmin)
#numerical apporx
f_IntNum = trapizoidal(fct_f, xmin, xmax, N)
#compare eaxact and numerical 
print('exact integral', f_IntExact),
print('num.approx', f_IntNum)
for current_n in range(10, 1000, 200):
    f_IntNum = trapizoidal(fct_f, xmin, xmax, N)
    print('increment dx' , float(xmax-xmin))
    print('exact integral', f_IntExact)
    print('num.approx', f_IntNum)