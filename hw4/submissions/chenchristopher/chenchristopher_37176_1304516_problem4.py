# -*- coding: utf-8 -*-
#python 2.7
"""
Find the roots of the 3 functions listed in problem 4
"""

import numpy as np

#==============================================================================
#variables
#==============================================================================
sampsize = 100
N = 100

#==============================================================================
#parameters
#==============================================================================
def fct1(x):
    return -x**5 + x**2 / 3 + 0.5 #for x between -10 and 10 exclusive

def fct2(x):
    return np.cos(x)**2 + 0.1 #for x between -10 and 10 exclusive

def fct3(x):
    return np.sin(x / 3) + 0.1 * (x + 5) #for x between -3 and 3 exclusive

#==============================================================================
#function definitions
#==============================================================================
def my_Secant(fct, x0, x1, tol, N):
    """
    Uses the secant method to find the roots of a function.
    Input: fct = function you want to find roots of
           x0 = one of your initial endpoint guesses
           x1 = the other initial endpoint guess
           tol = the accepted error of the root
           N = max number of iterations before giving up if no convergence
    Output: root of a function
    """
    x0 = float(x0)
    x1 = float(x1)
    i = 0
    while abs(fct(x1)) > tol and i < N:
        #numerical approximation of derivative
        dfdt = (fct(x1) - fct(x0)) / (x1 - x0)
        #basically Newton's method
        x_next = x1 - fct(x1) / dfdt
        x0 = x1
        x1 = x_next
        i += 1
    
    #Check for convergence
    if abs(fct(x1)) < tol:
        return x_next
    else:
        return np.nan
    
#==============================================================================
#computations
#==============================================================================
def findroots(fct, tmin, tmax, tol):
    sol = [] #array of roots for the different sampling points
    uni = [] #the amount of unique roots
    samp = np.linspace(tmin, tmax, sampsize)
    #put all roots into array sol
    for i in range(sampsize - 1):
        sol.append(round(my_Secant(fct, samp[i], samp[i + 1], tol, N), 2))
        #check how many unique roots there are and put them in array uni
        if not(sol[i] in uni) and (sol[i] * 0 == 0):
            uni.append(sol[i])
    #printing
    print('There is/are ' + str(len(uni)) + ' root(s).')
    print('They are (using secant method):')
    for i in uni:
        print('t = ' + str(i))
        
print('Function 1:')
findroots(fct1, -10, 10, 1e-6)
print('')

print('Function 2:')
findroots(fct2, -10, 10, 1e-6)
print('')

print('Function 3:')
findroots(fct3, -3, 3, 1e-6) 
print('')

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        