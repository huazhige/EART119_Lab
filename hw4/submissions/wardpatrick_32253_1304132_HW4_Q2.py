# -*- coding: utf-8 -*-

"""

Q2:
    

"""
import numpy as np
import matplotlib.pyplot as plt 
import os

c  = 1.1
t0 = 2.5
A  = 5

t = np.arange(-10, 11)

def zero(t):
    return t*0
def ft(t):
    return c*(t-t0)**2
def gt(t):
    return A*t + t0

def funct(t):
    return ft(t) - gt(t)
def dfdt(t):
    return c*2*t*(t-t0) - A

def my_Newton( fct, df_dt, x0, tol = 1e-4, N = 100):
    """
    :param fct:     - find root of this fct. closes to x0
    :param dfct_dt: - derivatice of fct
    :param x0:      - initial guess of solution
    :param N:       - number of iterations, default = 20
    :param tol:     - tolerance, default = 1e-4
    :return: f_r0 - closest to x0
    """
    xn = float( x0)
    i  = 0
    while abs( fct( xn)) > tol and i < N: # could also set fct. to ~0 to find root instead of min.
        x_next = xn - fct( xn)/df_dt( xn)
        print i, abs( fct( xn)), x_next
        xn = float( x_next)
        i += 1
    if abs( fct( xn)) > tol:# no solution found
        return None
    else:
        return float( x_next)



plt.plot(t, funct(t), label = 'f(t)-g(t)')
plt.plot(t, zero(t), 'k-', label = 'Zero')
#plt.plot(t, gt(t))


print my_Newton(funct, dfdt, 0)
print '\n'
print my_Newton(funct, dfdt, 9.108)


#value of intersection 
print '\nCrossover points -10<t<10: 2 \nValue of Intersection '

x1 = 0.436646434529
print 'x1:', 0.436646434529
print 'ft(x1):', ft(x1)
print 'gt(x1):', gt(x1)

x2 = 9.10880411471
print 'x2:', 9.10880411471
print 'ft(x2):', ft(x2)
print 'gt(x2):', gt(x2)

print '\n'

#==================================================
#             From inC_2_1
#==================================================
print 'From "inC2"'
tmin =-10
tmax = 10
iN = 200


a_t = np.linspace( tmin, tmax, iN)
## vectorized solution
a_ft  = ft(  a_t)
a_gt  = gt(  a_t)
a_g2t = funct( a_t)

#B#
a_df_g  = a_ft - a_gt
a_df_g2 = a_ft - a_g2t
## find all cross-over points
sel = abs(a_df_g) < 1e-4
## find minimum between fx - gx
sel_min = abs( a_df_g) == abs(a_df_g).min() # this results in a boolean array of 1 and 0
print 'cross over with min. distance: t=%s, f(t)=%s, g(t)=%s'%( a_t[sel_min], a_ft[sel_min], a_g2t[sel_min])


plt.plot( a_t, ft(  a_t), '-', mec = 'r', ms = 2, mfc = 'none', label = 'f(t)')
plt.plot( a_t, gt(  a_t), '-',     mec = 'b', ms = 2, mfc = 'none',  label = 'g(t)')
#plt.plot( a_t, g2_t( a_t, A, t0), 'o', mec = 'g', ms = 2, mfc = 'none',  label = 'g2(t)')
plt.xlabel( 't')
plt.ylabel( '')
plt.legend()
plt.show()

os.chdir( r'X:\ASTRO 119\Astro119\Homework 4')
plt.savefig( '2c cross')