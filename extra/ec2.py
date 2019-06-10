#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 18:46:22 2019

@author: williamdean
Extra Credit Problem 2
"""
import math
import numpy as np
import integrate_utils as int_utils

# parameters
N = 1000
xmin = 0
xmax_f = np.pi
xmax_g = 1
x_f = np.linspace( xmin, xmax_f, N)
x_g = np.linspace( xmin, xmax_g, N)
#================================================
#          fct definition
#================================================

def fct_f2( x):
    return np.sin( x)

def fct_g2( x):
    return 2*x*np.exp*(x**2)

# Computation of integrals
a_f = fct_f2( x_f)
a_g = fct_g2( x_g)

mvt_f = (fct_f2(xmax_f)-fct_f2(xmin))/(xmax_f - xmin)
mvt_g = (fct_g2(xmax_g)-fct_g2(xmin))/(xmax_g - xmin)
