# -*- coding: utf-8 -*-
"""
@author: Jason Minera

#2 find the intersection between two functions given and
find the value of the f(t) and g(t)
"""

#import matplotlib.pyplot as plt
#import numpy as np
import opt_utils as ou

def f_t(t):
    return (1.1*(t - 2.5)**2)
    
def df_t(t):
    return 2*1.1*(t - 2.5)


def g_t(t):
    return 5*t + 2.5

def dg_t(t):
    return 5

def f_minus_g(t):
    return f_t(t) - g_t(t)

def df_minus_g(t):
    return df_t(t) - dg_t(t)


#T  = np.linspace(-10, 10, 100) i tried using linspace to plot this



for t in range (-10, 0):
    ou.my_Newton(f_minus_g, df_minus_g, t, tol = 1e-4, N = 10)
print('****************Intersections occer at time above****************')
    #nextguess = guess - f_t(guess)/df_t(guess)
    #print(nextguess)
    #guess = nextguess
for t in range (0, 10):
    ou.my_Newton(f_minus_g, df_minus_g, t, tol = 1e-4, N = 10)
print('*************Intersections also occer at time above*************')    
    
    
    
    
#there are two zero values in these two functions
#at t = 0.436 and at t = 9.108
#now the values of f_t and g_t is

t1 = 0.436
t2 = 9.108

print ('F(t) values of the first intersection occurs at %f' %f_t(t1))
print ('F(t) values of the second intersection occurs at %f' %f_t(t2))

# i tried to plot this, wasnt working
'''
plt.subplot( t, f_t,'-')
plt.subplot(t, g_t, '-')
plt.xlabel('t(s)')
plt.ylabel('y(m)')

dx = np.argwhere(np.diff(np.sign(f_t - g_t))).flatten()
plt.plot(t[dx], f_t[dx], 'ro')
plt.show()
'''

