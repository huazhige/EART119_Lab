# -*- coding: utf-8 -*-
"""
Homework 4 Part 2 - Alex Watson
    - fine the crossover point(s) 
    between two functions f(t) & g(t)
    using Newton's/Secant method
"""
import numpy as np
import matplotlib.pyplot as plt

#==============================================================================
#                               fct def
#==============================================================================
def f_t( t, t0 = 2.5, c = 1.1):
    return c*(t-t0)**2

def g_t( t, t0 = 2.5, A = 5):
    return A*t + t0

def fct_diff( t, t0 = 2.5, c = 1.1, A = 5):
    return c*(t-t0)**2 - (A*t + t0)

def my_Secant( fct, x0, x1, tol = 1e-5, N = 20):
    x0 = float( x0)
    x1 = float( x1)
    i = 0
    while abs( fct(x1)) > tol and i < N:
        # numerical approx of derivative
        dfdt   = ( fct( x1) - fct( x0))/( x1 - x0)
        # basically Newton 
        x_next = x1 - fct( x1)/dfdt
        
        x0     = x1
        x1     = x_next
        
        i += 1
    # check if solution converged
    if abs( fct( x1)) > tol:
        return np.nan
    else:
        return x1
    
#==============================================================================
#                               Parameters
#==============================================================================
# var range
tmin = -10
tmax = 10

#==============================================================================
#                              find crossover pts
#==============================================================================
xover_pt = np.zeros(21)
iS = 0
for t in np.arange(tmin, tmax+1, 1):
    xover_pt[iS] = np.array( my_Secant( fct_diff, t, t+10))
    iS += 1
#==============================================================================
#                                   plot
#==============================================================================
a_t = np.linspace( tmin, tmax, 1000)

plt.figure( 1)
plt.plot( a_t, f_t( a_t), 'g-', label = 'f(t)=c(t-t0)^2')
plt.plot( a_t, g_t( a_t), 'b-', label = 'g(t)=At-t0')
plt.plot( [xover_pt[0]], [f_t(xover_pt[0])], 'r*', ms = 14, label = 'crossover points at t=%f & %f'%(xover_pt[0], xover_pt[20]))
plt.plot( [xover_pt[20]], [f_t(xover_pt[20])], 'r*', ms = 14)
plt.grid( True)
plt.xlabel( 't')
plt.ylabel( 'f(t), g(t)')
plt.legend( loc = 'upper left')
plt.show()
    
##A## How many crossover points are there?
print 'There are 2 crossover points within the specified range'

##B## What is the t, f(t) and g(t) values?
# NOTE: f(t) and g(t) should be exactly the same at these points since they cross over here,
# therefore there is no point in printing both f(t) and g(t) of these points.
print ('crossover points: (%5f, %5f) , (%5f, %5f)'
       %(xover_pt[0], f_t(xover_pt[0]), xover_pt[20], g_t(xover_pt[20]))) 
  
##C## Compare solutions to in-class assignment
plt.figure( 2)
plt.plot(a_t, fct_diff(a_t), 'k-', label = 'f(t)-g(t)')
plt.plot( [xover_pt[20]], [fct_diff(xover_pt[20])], 'r*', ms = 14, label = 'crossover points--Secant method')
plt.plot( 9.10, fct_diff( 9.10), 'b*', ms = 10, label = 'crossover points--in-class assignment')
plt.plot( [tmin, tmax], [0,0], 'r--')
plt.grid( True)
plt.xlabel( 't')
plt.ylabel( 'f(t)-g(t)')    
plt.legend( loc = 'upper left')  
file_in = 'Data/Watson_HW4_2.png'
plt.savefig( file_in, dpi = 150)  
plt.show()
    