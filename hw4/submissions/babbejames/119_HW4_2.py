#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 15:43:26 2019

HW4: #2

@author: jtbabbe
"""

import numpy as np
import matplotlib.pyplot as plt

#===================================================================
#           parameters
#===================================================================

t0   =   2.5
c    =   1.1
A    =   5.0
t    =   np.linspace(-10, 10, 2000) # set time steps from tmin to tmax 

#===================================================================
#           fct. def
#===================================================================

def ft( t):
    return c*(t-t0)**2 # fct 1

def gt( t):
    return (A*t) + t0 # fct2

fct = ft( t)
gct = gt( t)

def ft_gt( t):
    return (c*(t-t0)**2) - ((A*t) + t0) # difference between functions

def my_Secant( ft_gt, x0, x1, tol = 1e-5, N = 20):
    x0 = float( x0)
    x1 = float( x1)
    i=0
    while abs( ft_gt(x1)) > tol and i <N:
        # numerical approx of derivative
        dfdt = (ft_gt( x1) -ft_gt(x0))/(x1-x0)
        # same as Newton's methd
        x_next = x1 - ft_gt(x1)/dfdt
        
        x0 = x1
        x1 = x_next
        
        i += 1
    # check if solution coverged
    if abs(ft_gt(x1)) > tol:
        return np.nan
    else:
        return x1
        
#===================================================================
#           find t value of crossover points
#===================================================================

c1 = my_Secant(ft_gt, 0, 5, tol = 1e-5, N = 20)
c2 = my_Secant(ft_gt, 8, 10, tol = 1e-5, N = 20)

#===================================================================
#           find values of crossover points
#===================================================================

f1 = ft(c1)
g1 = gt(c1)
f2 = ft(c2)
g2 = gt(c2)

#===================================================================
#           Answers
#===================================================================

print()
print('Answers:')
print(' a)  There are 2 crossover points over this window. ')
print()
print(' b1: t1 =', c1, 'f(t1) =', f1, 'g(t1) =', g1)
print(' b1: t2 =', c2, 'f(t2) =', f2, 'g(t2) =', g2)
print()
print(' c) Secant Method: Red Stars.  Vectorized method: Blue Star.')

#===================================================================
#           Week 2 Portion

    
#===================================================================
#           Week 2 Parameters
#===================================================================

tmin, tmax = -10, 10
f_dt = 1e-2
iN = int( (tmax-tmin)/f_dt)

eps= 1e-1

#===================================================================
#           Week 2 Solution
#===================================================================

a_t = np.linspace( tmin, tmax, iN)
## vectorized solution
fct  = ft( t)
gct  = gt( t)

#B#
a_df_g  = fct - gct
## find all cross-over points
sel = abs(a_df_g) < eps
## find minimum between fx - gx
sel_min = abs( a_df_g) == abs(a_df_g).min()

#===================================================================
#           plot
#===================================================================

plt.figure(1)
plt.plot( t, ft( t), 'r-')
plt.plot( t, gt( t), 'b-')
plt.plot( c1, f1, 'r*', ms = 10)
plt.plot( c2, f2, 'r*', ms = 10)
plt.plot( a_t[sel_min], fct[sel_min], 'b*', ms = 10)
plt.savefig( 'Eart_119_hw4.2_plot.png')
plt.xlabel('t')
plt.ylabel('g(t) / f(t)')
plt.show

