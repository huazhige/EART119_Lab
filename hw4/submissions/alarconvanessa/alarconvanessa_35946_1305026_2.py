# -*- coding: utf-8 -*-
"""
Created on Sat May  4 21:24:42 2019
python/anaconda 3.7

HW week 5, problem 1
Comparing the Newton method to the method we used in week 2 to find cross 
over points

@author: Nessa
"""

import numpy as np
import matplotlib.pyplot as plt
import opt_utils as opt

#========================= defining functions==================================
def f_t(t):
    return 1.1*(t - 2.5)**2
def g_t(t):
    return 5*t + 2.5

#f(t) - g(t) where f(t) = 1.1*(t - 2.5)**2 and g(t) = 5*t + 2.5
def fct (t):
    return (1.1*(t - 2.5)**2) - (5*t + 2.5)

#f'(t) - g'(t) where f'(t) = 2.2*(t-2.5) and g'(t) = 5
def df_dt (t):
    return 2.2*(t-2.5) - 5

ax = np.array([])   

#where ax is array of cross over points.
for t in range (-10, 10):
    x = opt.my_Newton( fct, df_dt, t, tol = 1e-4, N = 20)
    ax = np.append(ax, x)
    t += 1

#get the cross over points of f(x) and g(x)
ax_round = np.around(ax, 4)
values = np.unique(ax_round)

#number of cross over points
numOFX = np.size(values)
print("A) Number of Cross over points: ", numOFX)

print('B) + C)')
for r in range (0, numOFX):
    print ('value of t at x-point', r + 1, ':', values[r])
    print ('value of f(x) at X-point', r + 1, ':', f_t(values[r]))
    print ('value of g(x) at x-point', r + 1, ':', g_t(values[r]))
    r += 1


#================= Week 2 Solution ============================================
tmin = -10
tmax = 10
iN = 250

a_t = np.linspace( tmin, tmax, iN)
eps= 1e-1
af_t = f_t(a_t)
ag_t = g_t(a_t)
sel = abs(fct(a_t)) < eps

print ('\n\nall t values of cross-over t = : ',a_t[sel],'\nf(t) at t:', af_t[sel], '\ng(t) at t:', ag_t[sel])
## find minimum between fx - gx
sel_min = abs(fct(a_t)) == abs(fct(a_t)).min() # this results in a boolean array of 1 and 0
print ('cross over with min. distance: t=%s,'%( a_t[sel_min]))

#make function plot
pvalues_t = np.linspace(-10, 10, endpoint = True)
yf_t = f_t(pvalues_t)
yg_t = g_t(pvalues_t)

plt.figure(1)
plt.title("Newton's method vs Week 2 method")
plt.plot(pvalues_t, yf_t, 'r-',  label = 'f(x)')
plt.plot(pvalues_t, yg_t, 'b-', label = 'g(x)')
plt.ylim(4.0, 5.0)
plt.xlim(0.42, 0.45)
plt.plot(a_t[sel], af_t[sel], 'g*', markersize = 12, label = 'Week 2 method')
plt.plot(values[0], f_t(values[0]), 'r*', markersize = 12, label = 'Newton method')
plt.legend(loc = 'best')

plt.show()
plt.savefig('ComparisonGraph')

"""
output:
    
    
A) Number of Cross over points:  2
B) + C)
value of t at x-point 1 : 0.4366
value of f(x) at X-point 1 : 4.683381516000001
value of g(x) at x-point 1 : 4.683
value of t at x-point 2 : 9.1088
value of f(x) at X-point 2 : 48.043861184000015
value of g(x) at x-point 2 : 48.044000000000004


all t values of cross-over t = :  [0.44176707 9.11646586] 
f(t) at t: [ 4.65995508 48.15538257] 
g(t) at t: [ 4.70883534 48.08232932]
cross over with min. distance: t=[0.44176707],
"""
