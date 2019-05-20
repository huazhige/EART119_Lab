#!python3

import numpy as np


#functions
f1 = lambda x: -x**5+1/3*x**2+1/2 
x1_min = -10
x1_max = 10
f2 = lambda x: (np.cos(x))**2 +0.1
x2_min = -10
x2_max = 10
f3 = lambda x: np.sin(x/3) + 0.1*(x+5)
x3_min = -3
x3_max = 3

#manual variables
error = 1e-4

#def
def secant(f, xmin, xmax, error):
    f0 = f(xmin)
    f1 = f(xmax)
    x0 = xmin
    x1 = xmax
    i = 0
    while abs(f1) > error and i < 100:
        if x1 - x0 == 0:
            print ('Error: x1 -x0 = 0')
            return None
        denominator = (f1 - f0)/(x1 - x0)
        if denominator == 0:
            print('Error: Denominator = 0)')
            return None
        if denominator == (f1 - f0)/(x1 - x0):
            x = x1 - f1/denominator
        x0 = x1
        x1 = x
        f0 = f1
        f1 = f(x1)
        i += 1
    return x
print('Equation 1:', secant(f1, x1_min, x1_max, error))
print('Equation 2:', secant(f2, x2_min, x2_max, error))
print('Equation 3:', secant(f3, x3_min, x3_max, error))




