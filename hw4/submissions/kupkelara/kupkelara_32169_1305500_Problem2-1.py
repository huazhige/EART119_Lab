
#!python3
import numpy as np
"""
Problem: Find cross-over points
f(t)=c(t−t0)**2
t0= 2.5
c = 1.1 

−10≤t≤10

g(t) = At +t0
A = 5

"""
#Given by the problem
t0= 2.5
c = 1.1 
A = 5
tstar = -10 
tend = 10

error = 1e-8

#cross-over when the difference btw. func. is zero
#difference = c*(t - t0)**2 - A*t - t0
#der_difference =  2*c*(t-t0)-A

def Newton(t, error,attempts, t0, c, A):
    #cross-over when the difference btw. func. is zero
    df =  2*c*(t-t0)-A
    for n in range(0,attempts):
        if abs(c*(t - t0)**2 - A*t - t0) < error:
            return t
        if 2*c*(t-t0)-A == 0:
            print('Zero derivative. No solution found.')
            return None
        t = t - (c*(t - t0)**2 - A*t - t0)/(2*c*(t-t0)-A)
    return answer
PointA = Newton(10, error, 100, t0, c, A)
PointB = Newton(-10, error, 100, t0, c, A)
print(PointA)
print (PointB)

"""
a) 2 cross over points
b)
"""
f = lambda t: c*(t - t0)**2 
g = lambda t: A*t + t0

print('f(t) is:', f(PointA), f(PointB))
print('g(t) is:', g(PointA), g(PointB))

N= 1000
a_t = np.linspace(-10,10,N)
plt.plot(a_t,f(a_t), 'ro', ms=2)
plt.plot(a_t, g(a_t), 'go', ms=2)
plt.show()

"""Not much of a difference to see for part c."""


#week 2 assignment
"""Determine the crossover point between two functions f(t) and g(t). 
1) as a for loop
2) vectorized problem using numpy
"""

import numpy as np
import matplotlib.pyplot as plt
#================================================
#               Parameters
#================================================
tmin, tmax = -10, 10
iN         = 1000
f_dt       = float(tmax-tmin)/(iN-1)

#fct parameters
t0  = 2.5
c   = 1.1
A   = 5
eps = 0.1

#================================================
#             functions def
#================================================
def f_t(t, c, t0):
    return c*(t - t0)**2
def g_t(t, A):
    return A*t + t0

#================================================
#               Find cross-over point
#===============================================
##A## for loop
f_curr_t = tmin
for i in range(iN):
    f_curr_t += f_dt
    f_curr_f_t = f_t(f_curr_t, c, t0)
    f_curr_g_t = g_t(f_curr_t, A)
    #fct value comparison
    if abs (f_curr_f_t - f_curr_g_t) < eps:
        print('cross over point at t=%.2f,f(t)=%.2f,  g(t)=%.2f'%(f_curr_t, f_curr_f_t, f_curr_g_t))
##B## Vectorized solution
a_t = np.linspace( tmin,tmax, iN)
#evaluate fct
a_ft= f_t(a_t, c, t0)
a_gt= g_t(a_t, A)
#find cross-over point
sel = abs(a_ft-a_gt) < eps
print ('cross over points', a_t[sel], a_ft[sel], a_gt[sel])


#================================================
#               Plot
#===============================================
plt.plot(a_t,a_ft, 'ro', ms=2)
plt.plot(a_t, a_gt, 'go', ms=2)
plt.show()


