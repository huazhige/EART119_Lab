# -*- coding: utf-8 -*-
"""
HOMEWORK 4 QUESTION 2
"""
import numpy as np
import matplotlib.pyplot as plt
import opt_utils
import os

data = 'C:\\Users\\Joey\\Desktop\\aapython'
tmin, tmax = -10, 10
f_dt = 1e-2
iN = int( (tmax-tmin)/f_dt)

def f_t(t):
    return 1.1*(t-2.5)**2 - (5*t + 2.5)

def g_t(t):
    return 5*t + 2.5

def df_dt(t):
    return 2*1.1*(t - 2.5) - 5

for t in range(-10,10):
    root = opt_utils.my_Newton(f_t, df_dt, t, tol = 1e-4, N = 20)
    t += 1

#2 crossover points based on my_Newton output
t1 = 0.4366
t2 = 9.108

f_t1 = 1.1*(.4366-2.5)**2
f_t2 = 1.1*(9.108-2.5)**2

print 'Crossover Points: '
print 't1,f(t1),g(t1): ' + str(t1) + ' ' + str(f_t1) + ' ' + str(g_t(t1))
print 't2,f(t2),g(t2): ' + str(t2) + ' ' + str(f_t2) + ' ' + str(g_t(t2))
        
#---------------------------------------------------------------
#               PART C
#---------------------------------------------------------------
plt.figure(1)
a_t = np.linspace(tmin,tmax,iN)
plt.plot(a_t, f_t(a_t))

#CROSSOVER POINTS COMPARED
plt.plot(0.4366, 4.683, 'x')
plt.plot(.4352, 4.6897, 'o')

plt.xlabel('t')
plt.ylabel('f(t)-g(t)')
plt.legend()
plt.show()

os.chdir( data)
plt.savefig( 'dir_out')