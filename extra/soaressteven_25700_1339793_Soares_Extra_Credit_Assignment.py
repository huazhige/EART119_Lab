# -*- coding: utf-8 -*-
#python2.7

from __future__ import division

import numpy as np
import integrate_utils as int_utils

# =============================================================================
#                           Define functions
# =============================================================================

# For part 1.

def f1 ( t):
    return 3*t**2*np.exp(t**3)
 
def F1 ( t):
    return np.exp(t**3)

# For part 2.

# For part a.
    
def f2 ( x):
    return np.sin(x)

def F2 ( x):
    return np.cos(x)

# For part b.
    
def g2 ( x):
    return 2.*x * np.e**(x**2.)

def G2 ( x):
    return np.e**(x**2.)

# For part 3.

# For part a.
    
def f3 ( x, y):
    return (x**2. + y**2.)**(0.5)

def g3( x, y):
    f_retVal = -1
    if x >= xmin and x <= xmax and y >= ymin and y <= ymax:
        f_retVal = 1
    return f_retVal

def F3 ( r, theta):
    return theta * (0.5 * r**2.)

# Functions for part b.
    
def w3 ( x, y):
    return x*y**2.

def W3 ( x, y):
    return (0.5 * x**2.) * ((1/3.) * y**3.)

# =============================================================================
#                          Define parameters
# =============================================================================

N = 100
N2 = 1000

# For part a.

t1 = np.linspace(0,1,N)
sol_exact1 = F1(t1[N-1]) - F1(t1[0])

# For part b.

x2a = np.linspace(0, np.pi,N2)
sol_exact2a = F2(x2a[N2-1]) - F2(x2a[0])

x2b = np.linspace(0, 1, N2)
sol_exact2b = G2(x2b[N2-1]) - G2(x2b[0])

# For part c.

r3 = np.linspace(0, 2, N)
theta3 = np.linspace(0, np.pi, N)
sol_exact3a = F3(r3[N-1], theta3[N-1]) - F3(r3[0], theta3[0])
x3 = np.linspace(0, 2, N)
y3 = np.linspace(0, 1.5, N)
sol_exact3b = W3(x3[N-1], y3[N-1]) - W3(x3[0], y3[0])

# =============================================================================
#                             Integration
# =============================================================================

# For part 1.

num_sol_1_midpoint = int_utils.midpoint( f1, t1[0], t1[N-1], N)
num_sol_1_trapezoid = int_utils.trapezoidal( f1, t1[0], t1[N-1], N)

# For part 2.



# For part 3.

num_sol3a = int_utils.monteCarlo( w3, g3, -2, 2, -2, 2, N2)
num_sol3b = int_utils.monteCarlo( f3, g3, -1, 3, -1, 2.5, N2)

# =============================================================================
#                                 Comparisons
# =============================================================================

# For part 1.

print('Midpoint Method: %4.4f, Trapezoid Method: %4.4f,  Exact Solution: %4.4f'%(num_sol_1_midpoint, num_sol_1_trapezoid, sol_exact1))

# For part 2.

#print()

# For part 3.

print('Montecarlo Integration (3a): %4.4f, Exact Solution: %4.4f'%(num_sol3a, sol_exact3a))
print('Montecarlo Integration (3b): %4.4f, Exact Solution: %4.4f'%(num_sol3b, sol_exact3b))