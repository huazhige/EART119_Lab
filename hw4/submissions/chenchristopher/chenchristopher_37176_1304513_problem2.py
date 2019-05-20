# -*- coding: utf-8 -*-
#python 2.7
"""
Find the intersection (cross-over point) between the following two functions using Newton’s or the Secant method
f(t) - g(t) for t between -10 and 10 inclusive
"""

import numpy as np
import matplotlib.pyplot as plt

#==============================================================================
#parameters
#==============================================================================
tmin, tmax = -10, 10
t0 = 2.5
c = 1.1
A = 5
tol = 1e-6
eps = 0.1
N = 100
sampsize = 1000
samp = np.linspace(tmin, tmax, sampsize) #sample intervals along our function
sol = [] #array of roots for the different sampling points
uni = [] #the amount of unique roots

#function f
def fct_f(t):
    return c * (t - t0)**2

#function g
def fct_g(t):
    return A * t + t0

#difference of both functions
def fct_diff(t):
    return fct_f(t) - fct_g(t)

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

def my_Newton(fct, df_dx, x0):
    """
    implementation of Newton's method for solving for roots when f'(x) is known
    """
    N = 20
    i = 0
    xn = float(x0)
    eps = 1e-6
    while fct(xn) < eps or i < N:
        x_next = xn - fct(xn) / df_dx(xn)
        xn = x_next
        i += 1
    if abs(fct(xn)) < eps:
        return x_next
    else: #solution did not converge
        return np.nan
    
#==============================================================================
#computations
#==============================================================================
#put all roots into array sol
for i in range(sampsize - 1):
    sol.append(round(my_Secant(fct_diff, samp[i], samp[i + 1], tol, N), 3))
    #check how many unique roots there are and put them in array uni
    if not(sol[i] in uni):
        uni.append(sol[i])

#compare with method of creating two arrays with the functions and making a difference array
#and then finding how many zeroes there are
a_ft = fct_f(samp)
a_gt = fct_g(samp)
sel = abs(a_ft - a_gt) < eps

#==============================================================================
#printing
#==============================================================================
print('There are ' + str(len(uni)) + ' roots.')
print('They are (using secant method):')

for i in uni:
    print('t = ' + str(i) + ' with f(t) = ' + str(fct_f(i)) + ', g(t) = ' + str(fct_g(i)))

print('Crossover points using array method:')    
print('Arrays of t, f(t), and g(t) values respectively', samp[sel], a_ft[sel], a_gt[sel])
print('The graph shows the difference function and two points for the calculated root using the two different methods. The black dot is a root calculated from the secant method and the red is from the array method.')

#==============================================================================
#plotting
#==============================================================================
plt.plot(samp, a_ft - a_gt, 'go', ms = 2)
plt.plot(uni[0], fct_f(uni[0]), 'ko')
plt.plot(samp[sel][0], a_ft[sel][0] - a_gt[sel][0], 'ro')
plt.savefig('graphrootcomparison.png')
plt.show()