# Allison Swart
# Astro/Earth 119 Homework #4
# May 5, 2019

#anaconda2/python2.7

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#               Problem 1
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#python2.7

"""
-  create  temperature profile that follows:
    T_i = f_Tm + Acos( 2pi/w * t - phi)
    with some Gaussian error
"""

import numpy as np
import matplotlib.pyplot as plt
import os
#==============================================================================
#                             fct definitions
#==============================================================================
def fct_T( t, Tm, A):
    return Tm + A*np.cos( (2*np.pi)/w * t)
np.random.seed(123456)
#==============================================================================
#                               params
#==============================================================================
dir_out = 'data'
file_out= 'Hw4_1_fixed.png'
N       = 1000
f_Tm    =  10 # mean T in C
f_dA    =  40  # in degree 
w       =  3600 # noise / error
f_sigma = 15.2
#==============================================================================
#                           create synthetic data
#==============================================================================
a_t = np.linspace( 0, 7*w) # convert to martian days
a_T = fct_T( a_t, f_Tm, f_dA)# add some noise
a_T_noise = a_T + np.random.randn(  N)*f_sigma
#==============================================================================
#                              save to file
#==============================================================================
fig, ax = plt.subplots()
plt( a_t, a_T_noise, 'ko', ms = 2)
plt( a_t, a_T, 'r-', lw = 1.5)
# save this figure as .png

os.chdir( 'dir_out')
plt.savefig( 'dir_out')
plt.show()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#              Problem 2
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def f_t( t):
    t0 = 2.5
    c = 1.1
    return c*(t - t0)**2

def dfdt( t):
    c = 1.1
    t0 = 2.5
    return 2*c*t - 2*t0

def g_t( t):
    A = 5
    t0 = 2.5
    return A*t + t0

def dgdt( t):
    A = 5
    return A

def my_Newton( f_t, dfdt, t0):
    #used to solve f(x) = 0 when f' is known
    t0 = 2.5
    tn = float( t0)
    eps = 1e-5
    N = 20
    i = 0
    while f_t( tn) > eps and i < N:
        t_next = tn - f_t( tn) / dfdt( tn)
        t_next = tn
        i += 1
    if abs( f_t( tn)) < eps:
         t_next = tn - f_t( tn) / dfdt( tn)
         t_next = tn
         return t_next
    else: #solution did not converge
        return np.nan

t0 = 2.5
tmin, tmax = -10, 10
f_root_N = my_Newton( f_t, dfdt, t0)
g_root_N = my_Newton( g_t, dgdt, t0)
cross_over = f_root_N - g_root_N


a_t = np.linspace( tmin, tmax, 1000)

plt.figure(1)
plt.plot( a_t, f_t(a_t), 'k-')
plt.plot( a_t, g_t(a_t), 'b-')
plt.plot( [f_root_N], [f_t( f_root_N)], 'b*', ms = 10)
plt.plot( cross_over, 'r*')
plt.plot( [tmin, tmax], [0, 0], 'r--')
plt.grid( True)
plt.xlabel( 't')
plt.ylabel( 'Fct values f(t)')
plt.show()

# PART A

"""
Two points for -10 < x < 10
"""

# PART B

"""
t = .4365 & 9.109
f(t) = 4.7 & 48.04
g(t) = 4.7 & 48.04
"""

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#              Problem 3
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def fct( x):
    return -x**2 + 10*x + 9

def dfdx( x):
    return -2*x + 10

def my_Newton( fct, dfdx, x0):
    #used to solve f(x) = 0 when f' is known
    xn = float( x0)
    eps = 1e-6
    N = 20
    i = 0
    while (fct( x0**( i + 1)) - fct( x0**i)) < eps:
       x_next = xn - fct( xn) / dfdx( xn)
       #print( i, 'fct_value', abs( fct( xn)), x_next)
       xn = x_next
       i += 1
    if abs(fct( x0**(i + 1)) - fct( x0**i)) < eps and i < N:
        return xn
    else: #solution did not converge
        return np.nan
    
x0 = -9
root = my_Newton( fct, dfdx, x0)
print root


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#              Problem 4
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def my_Secant( fct, x0, x1, tol = 1e-5, N = 20):
    # when we don't know f'
    x0 = float( x0)
    x1 = float( x1)
    i = 0
    while abs( fct( x1)) > tol and i < N:
        #numerical approximation
        dfdt = (fct( x1) - fct( x0)) / (x1 - x0)
        x_next = x1 - fct( x1) / dfdt
        
        x0 = x1
        x1 = x_next
        i += 1
    #check for convergence
    if abs( fct( x1)) > tol:
        return np.nan
    else:
        return x1

def fct_1( x):
    return -x**5 + (1/3)*x**2 + (1/2)

def fct_2( x):
    return (np.cos( x))**2 + 0.1

def fct_3( x):
    return np.sin( x / 3) + 0.1*( x + 5)

x0 = -9
xmin, xmax = -10, 10

root_fct_1 = my_Secant( fct_1, x0, x0 + 10)
root_fct_2 = my_Secant( fct_2, x0, x0 + 10)
root_fct_3 = my_Secant( fct_3, x0, x0 + 10)

print 'Function 1 = ', root_fct_1
print 'Function 2 = ', root_fct_2
print 'Function 3 = ', root_fct_3


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#              Problem 5
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

vertical_trajectory = np.loadtxt( 'VertTraj.txt')

delta_t = 0.1
a_t = np.arange( 0, 0 + delta_t, delta_t)


def velocity( v0, t):
    disp = v0*t + 0.5*t**2
    dzdt_CD = (disp( a_t + delta_t) - disp( a_t - delta_t)) / delta_t
    dzdt_CD = (vertical_trajectory[2::] - vertical_trajectory[0:-2]) / (2 * delta_t)
    return dzdt_CD

def acceleration( v0, t):
    vel = v0 + t
    dzdt_CD = (vel( a_t + delta_t) - vel( a_t - delta_t)) / delta_t
    dzdt_CD = (vertical_trajectory[2::] - vertical_trajectory[0:-2]) / (2 * delta_t)
    return dzdt_CD

instantanious_v = velocity( vertical_trajectory[1], vertical_trajectory[2])
print 'Velocity = ', instantanious_v

instantanious_a = acceleration( vertical_trajectory[1], vertical_trajectory[2])
print 'Acceleration = ', instantanious_a