# -*- coding: utf-8 -*-
"""
Created on Thu May  2 18:13:09 2019

@author: blchapma
"""

import numpy as np
from matplotlib import pyplot as plt
import os


#========================================================================================================================
" Question 2"
""" Find the intersection (cross-over point) between the following two functions using
Newton’s or the Secant method (Hint: solve for 𝑓(𝑡) − 𝑔(𝑡) = 0)! 
"""
#========================================================================================================================


'Variables'
tmin, tmax = -10, 10
f_dt = 1e-2
iN = int( (tmax-tmin)/f_dt)

t0 = 2.5
c  = 1.1
A  = 5
eps= 0
testPlot = True



"Functions"
def f_t( t, c, t0):
    return c*(t - t0)**2

def g_t( t, A):
    return A*t + t0

def g2_t( t, A, t0):
    return A*t**2 + t0


#===================================================================================
#                         Find intersections
#===================================================================================
"Variables"
f_curr_t = tmin
for x in range( iN):
    f_curr_t += f_dt
    f_curr_gt = g_t( f_curr_t, A)
    f_curr_ft = f_t( f_curr_t, c, t0)
    if abs( f_curr_ft - f_curr_gt) == eps:
        print( 'cross-over point at t=%.2f, g(t) = %.2f, f(t) = %.2f'%( f_curr_t,f_curr_gt, f_curr_ft))

"plotting"
a_t = np.linspace( tmin, tmax, iN)
## vectorized solution
a_ft  = f_t(  a_t, c, t0)
a_gt  = g_t(  a_t, A)
a_g2t = g2_t( a_t, A, t0)

#B#
a_df_g  = a_ft - a_gt
a_df_g2 = a_ft - a_g2t
## find all cross-over points
sel = abs(a_df_g) < eps
print ('all cross-over points:, ',a_t[sel], a_ft[sel], a_g2t[sel])
## find minimum between fx - gx
sel_min = abs( a_df_g) == abs(a_df_g).min() # this results in a boolean array of 1 and 0
print ('cross over with min. distance: t=%s, f(t)=%s, g(t)=%s'%( a_t[sel_min], a_ft[sel_min], a_g2t[sel_min]))

## test plot
if testPlot == True:
    # plt.plot( a_t, abs(a_df_g),  'o', mec = 'r', ms = 2, mfc = 'none', label = '|f - g|')
    # plt.plot( a_t, abs(a_df_g2), 'o', mec = 'b', ms = 2, mfc = 'none', label = '|f - g2|')
    # plt.plot( [tmin, tmax], [0,0], 'k--')
    # plt.xlabel( 't')
    # plt.ylabel( 'Error Function')

    plt.plot( a_t, f_t( a_t, c, t0), 'o', mec = 'r', ms = 2, mfc = 'none', label = 'f(t)')
    plt.plot( a_t, g_t( a_t, A), 'o',     mec = 'b', ms = 2, mfc = 'none',  label = 'g(t)')
    #plt.plot( a_t, g2_t( a_t, A, t0), 'o', mec = 'g', ms = 2, mfc = 'none',  label = 'g2(t)')
    plt.xlabel( 'f(t)')
    plt.ylabel( 'g(t)')
    plt.legend()
    plt.show()


"Question 2"

"A. 3 crossover points"

"""B. cross-over point at t=0.36, g(t) = 5.02, f(t) = 5.04
cross-over point at t=0.37, g(t) = 5.09, f(t) = 4.99
all cross-over points:,  [0.35517759 0.36518259] [5.06028949 5.01318991] [3.38305784 3.43350827]
cross over with min. distance: t=[0.36518259], f(t)=[5.01318991], g(t)=[3.43350827]"""

"C."

plt.savefig('plot.png', bbox_inches_="tight")

