#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May 13 18:33:52 2019
    EART/ASTR 119

@author: Andrew Quartuccio
"""
# =============================================================================
#               Imports
# =============================================================================

import numpy as np
import matplotlib.pyplot as plt
#self
import Modules.integrate_utils as int_utils

# =============================================================================
#               Parameters
# =============================================================================

N      = 1000
xmin   = 0.0
xmax_f = np.pi
xmax_g = 1.0
x_f    = np.linspace(xmin, xmax_f, N)
x_g    = np.linspace(xmin, xmax_g, N)

# =============================================================================
#               f(x) & g(x) Definitions
# =============================================================================

def fct_f(x):
    return np.sin(x)

def fct_g(x):
    return 2*x*np.exp(x**2)

# =============================================================================
#               Computation of Integrals
# =============================================================================

#   Functions Evaluated at N nodes between xmin and xmax

a_fx = fct_f(x_f)
a_gx = fct_g(x_g)

#   MVT Solutions of Functions over domain

mvt_fx = (fct_f(xmax_f) - fct_f(xmin)) / (xmax_f - xmin)
mvt_gx = (fct_g(xmax_g) - fct_g(xmin)) / (xmax_g - xmin)
#
#print(fct_f(xmax_f))
#print(fct_f(xmin))
#print(fct_g(xmax_g))
#print(fct_g(xmin))




#   Numerical Solutions of Integrals

intTrapz_f = int_utils.trapezoidal(fct_f, xmin, xmax_f, N)
intMidpt_f = int_utils.midpoint(fct_f, xmin, xmax_f, N)

intTrapz_g = int_utils.trapezoidal(fct_g, xmin, xmax_g, N)
intMidpt_g = int_utils.midpoint(fct_g, xmin, xmax_g, N)

print('mvt f = ', mvt_fx)
print('mvt g = ', mvt_gx)
print('Trapz f = ', intTrapz_f)
print('Midpt f = ', intMidpt_f)

print('Trapz g = ', intTrapz_g)
print('Midpt g = ', intMidpt_g)

#   functions plotted
ax1 = plt.subplot(211)
plt.plot(x_f, a_fx, 'r-')
ax1.set_ylabel('f(x)')
#plt.axis([0, 1, 0, 10])
plt.fill_between(x_f, 0, a_fx, facecolor = 'blue')

ax2 = plt.subplot(212)
plt.plot(x_g, a_gx, 'g-')
ax2.set_xlabel('Independent Variable - x')
ax2.set_ylabel('g(x)')
#plt.axis([0, 1, 0, 10])
plt.fill_between(x_g, 0, a_gx, facecolor = 'red')
plt.show()

