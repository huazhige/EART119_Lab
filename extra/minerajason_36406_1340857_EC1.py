# -*- coding: utf-8 -*-
"""
@author: Jason

1. Compute the integral of the following function within the given domain.
Use both midpoint and trapezoidal methods! Compare your results to the exact 
solution of the definite integral

a.) f(t) = 3t**2*e**t**3 
"""

import numpy as np
import integrate_utils as iu



def ft(t):
    return 3*(t**2)*np.exp(t**3)


def integration_ft(t):
    return np.exp(t**3)


sol = integration_ft(1) - integration_ft(0)

trapazoidal = iu.trapezoidal(ft, 0, 1, 100)
midpoint = iu.midpoint(ft, 0, 1, 100)


print'solution: ', sol
print'Trapezoidal method: ', trapazoidal
print'Difference', sol - trapazoidal
print'Midpoint method: ', midpoint
print'Difference ', (sol - midpoint)
