# -*- coding: utf-8 -*-
"""
Problem 2
    Find the intersection (cross-over point) between the following two functions using
    Newton’s or the Secant method (Hint: solve for �(�) − �(�) = 0)!
    • �(�) = �(� − �*)+,	with	t0 =	2.5,	c	=	1.1,	and	−10 ≤ t ≤ 10
    • �(�) = �� + �*,	with A =	5,																								and	−10 ≤ t ≤ 10
    a) How many cross-over points are there for −10 ≤ t ≤ 10?
    b) What are the values of t, �(�) and �(�)?
    c) Compare your solutions with the solution from week 2 (in class assignment
    inC_2_1_vec_matrix.pdf, functions and vectors). For the comparison:
    plot �(�) − �(�) and one of the cross-over points detected with both methods.
    You may have to zoom a bit to see the difference. Save the plot as .png and
    submit to canvas.
    
    
    For answers run the program and it spits it out in print statement
"""
import numpy as np
import matplotlib.pyplot as plt

import opt_utils as opt_utils

t0 = 2.5
c = 1.1
A = 5.
t = np.linspace(-10,10,1000)

troot = [0.3, 9]
print("Two cross over points from -10 < t < 10\n------------------")

def f_t( t, t0, c):
    return c*(t-t0)**2

def g_t( t, t0, A):
    return A*t + t0


def fg_t (t):
    c = 1.1
    A = 5
    return c*t**2 - (A+2*c*t0)*t + c*t0**2 - t0
def dfgdt(t):
    c = 1.1
    A = 5
    return 2*c*t - A -2*c

cross = []
for i in troot:
    troot = opt_utils.my_Newton( fg_t, dfgdt, i)
    print("-----------\nf(t) = %s and g(t) = %s at t = %s\n-----------"%(f_t(troot, t0, c), g_t(troot, t0, A), troot))
    cross.append(troot)
    


##########in class assignment

#==============================================================================
#               Parameters
#==============================================================================
tmin,tmax = -10,10
iN        = 1000
f_dt      = float(tmax-tmin)/iN

#function parrameters
t0 = 2.5
c  = 1.1
A  = 5.
eps= 0.1

#==============================================================================
#               Function Definition
#==============================================================================
def oldf_t(t,c,t0):
    return c*(t-t0)**2

def oldg_t(t,A,t0):
    return A*t+t0
#################


#==============================================================================
#               Find Crossover point
#==============================================================================

##A## For Loop Solution
print("=====================\nFrom Week 2:")
f_curr_t = tmin
old_t = []
old_ft = []
for i in range(iN):
    f_curr_t += f_dt
    f_curr_f_t = oldf_t(f_curr_t,c,t0)
    f_curr_f_g = oldg_t(f_curr_t,A,t0)
    #function value comparison
    if abs(f_curr_f_t - f_curr_f_g) < eps:
        print("cross over point at t=%.2f, f(t)=%.2f, g(t)=%.2f"%(f_curr_t,f_curr_f_t,f_curr_f_g))
        old_t.append(f_curr_t)
        old_ft.append(f_curr_f_t)
##B## Vectorized Solution
a_t = np.linspace( tmin,tmax,iN)
#evaluate function 
a_ft = oldf_t(a_t,c,t0)
a_gt = oldg_t(a_t,A,t0)
#find cross over
sel = abs(a_ft-a_gt) < eps
print("cross over points:%s %s %s"%(a_t[sel], a_ft[sel], a_gt[sel]))

#==============================================================================
#               Plot functions
#==============================================================================

plt.plot(a_t,a_ft,'r-',ms=2)
plt.plot(a_t,a_gt,'g-',ms=2)
for new_cross in cross:
    plt.plot([new_cross], f_t(new_cross, t0 , c), 'r*', ms = 14) 
    
for old_cross in range (len(old_t)):
    plt.plot(old_t[old_cross], old_ft[old_cross], 'b*', ms = 10)
    
plt.legend(('f(t)','g(t)','Newtons Method','Newtons Method', 'Old Method', 'Old Method'), loc = 'upper right')
plt.plot()
plt.show()