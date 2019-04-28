# -*- coding: utf-8 -*-
"""
                                Homework 1: Problem 3
                                    Alex Watson
    - use a while loop to determine maximum b, where ab < area of circle with defined radius
"""
import numpy as np
import math
#==============================================================================
#                                   Variables
#==============================================================================

r = 12.6
a = 1.5
n = 10000

# Calculated area

A_circ = math.pi*r**2
A_rec  = np.linspace(0, A_circ, n)

#==============================================================================
#                                  Solve for b
#==============================================================================

#While loop
i = 1

while A_rec[i] < A_circ:
    largest_b = A_rec[i]/a
    i += 1

print('maximum length of side b: %10.2f mm'%( largest_b))