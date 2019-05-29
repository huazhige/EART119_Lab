#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May 6 07:55:49 2019
    EART/ASTR 119

    Numerical Integration of definite Integrals
        by using Trapezoidal& Midpoint Method

@author: Andrew Quartuccio
"""

# =============================================================================
#              Imports
# =============================================================================

import numpy as np
import matplotlib.pyplot as plt
import Modules.integrate_utils as int_utils


# =============================================================================
#               f(x) Definitions
# =============================================================================

def fct_f(t):
    return 3*t**2*np.exp(t**3)

def fct_df(t):
    return np.exp(t**3)

# =============================================================================
#               Parameters
# =============================================================================

xmin =   0.0
xmax =   1.0
N    = 100
t    = np.linspace(xmin, xmax, N)

# =============================================================================
#               Num. Integration (Midpoint & Trapz) and Plotting
# =============================================================================

#   Exact Solution
f_IntExact = fct_df(xmax) - fct_df(xmin)

#   Plotting Solution
a_f  = fct_f(t)
a_df = fct_df(t)

#   Numerical Approx. using Trapezoidal Method
f_IntNum_trap = int_utils.trapezoidal(fct_f, xmin, xmax, N)

#   Numerical Approx. using Midpoint Method
f_IntNum_mid  = int_utils.midpoint(fct_f, xmin, xmax, N)

#   Compare Exact and Numerical
print('Exact Integral: %45.16f')% (f_IntExact)
print('Numerical Approximation [Trapz Method]:    %16.16f')% (f_IntNum_trap)
print('Numerical Approximation [Midpoint Method]: %16.16f')% (f_IntNum_mid)
print('Difference between Trapz and Exact: %25.16f')% (abs(f_IntExact-f_IntNum_trap))
print('Difference between Mid and Exact: %27.16f')% (abs(f_IntExact-f_IntNum_mid))
print('Percent accuracy gained: %36.16f')% ((abs(f_IntExact-f_IntNum_trap)
        - abs(f_IntExact-f_IntNum_mid))/(abs(f_IntExact-f_IntNum_trap)) * 100)

# =============================================================================
# for curr_n in range(10,1000,20):
#     f_IntNum_trap = int_utils.trapezoidal(fct_f, xmin, xmax, curr_n)
#     print(curr_n, f_IntNum_trap)
#
# =============================================================================

#   Plot the two functions
plt.figure(1, figsize = (10,6))

ax1 = plt.subplot(211)
plt.plot(t, a_f, 'r-')
ax1.set_ylabel('f(t)')
plt.axis([0, 1, 0, 10])
plt.fill_between(t, 0, a_f, facecolor = 'blue')

ax2 = plt.subplot(212)
plt.plot(t, a_df, 'g-')
ax2.set_xlabel('Independent Variable - t')
ax2.set_ylabel('F(t)')
plt.axis([0, 1, 0, 10])
plt.fill_between(t, 0, a_df, facecolor = 'red')
plt.show()
