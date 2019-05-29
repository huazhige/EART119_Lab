import numpy as np

def func(t):
    return 3*(t**2)*np.exp(t**3)

def trapezoidal(  fct_x, x0, xn, N):
    dx = float(xn-x0)/N
    f_Int  = 0.5*(fct_x( x0) + fct_x( xn)) + ( fct_x( x0+dx*np.arange(1, N, 1))).sum()
    return dx*f_Int

def midpoint( fct_x, x0, xn, N):
    dx     = float( xn-x0)/N
    a_xi   = x0 + 0.5*dx + np.arange( N)*dx
    f_int  = dx*( fct_x(a_xi)).sum()
    return f_int

true = 1.71828
trap = trapezoidal(func, 0, 1, 10)
mid = midpoint(func, 0, 1, 10)

print("Trapezoidal Method: " + str(trap) + " which is " + str(abs(trap-true)) + " off of the actual value.")
print("Midpoint Method: " + str(mid) + " which is " + str(abs(mid-true)) + " off of the actual value.")