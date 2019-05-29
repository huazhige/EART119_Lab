# Extra Credit

# Allison Swart
# May 19, 2019

import numpy as np

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                      Problem 1
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def f_t( t):
    return 3*t**2*np.e**t**3

def trapezoidal(  f_t, x0, xn, N):
    """
    :param fct_x:  - function whose integral is in question
    :param x1:     - integration bounds
    :param x2:     - integration bounds
    :param N:      - number of trapezoids, chose high number for high accuracy
    :return:       - integral of fct_x between x0 and xn
    """
    dx = float(xn-x0)/N
    f_Int  = 0.5*(f_t( x0) + f_t( xn)) + ( f_t( x0+dx*np.arange(1, N, 1))).sum()
    # # as a for loop
    # f_Int  = 0.5*(fct_x( x0) + fct_x( xn))
    # for i in range( 1, N):
    #     f_Int += fct_x( x0 + i*dx)
    # print( f_Int*dx)
    return dx*f_Int

def midpoint( f_t, x0, xn, N):
    """
    :param fct_x:  - function whose integral is in question
    :param x1:     - integration bounds
    :param x2:     - integration bounds
    :param N:      - number of trapezoids, chose high number for high accuracy
    :return:       - integral of fct_x between x0 and xn
    """
    dx     = float( xn-x0)/N
    a_xi   = x0 + 0.5*dx + np.arange( N)*dx
    f_int  = dx*( f_t(a_xi)).sum()
    return f_int

exact_solution = np.e - 1

trapezoidal_solution = trapezoidal( f_t, 0, 1, 100)
print 'Trapezoidal Solution = ', trapezoidal_solution
midpoint_solution = midpoint( f_t, 0, 1, 100)
print 'Midpoint Solution = ', midpoint_solution
print 'Exact Solution = ', exact_solution

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                    Problem 2
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def f_x_a( x):
    return np.sin( x)

def f_x_b( x):
    return 2*x*np.e**x**2

def midpoint( f_x, x0, xn, N):
    """
    :param fct_x:  - function whose integral is in question
    :param x1:     - integration bounds
    :param x2:     - integration bounds
    :param N:      - number of trapezoids, chose high number for high accuracy
    :return:       - integral of fct_x between x0 and xn
    """
    dx     = float( xn-x0)/N
    a_xi   = x0 + 0.5*dx + np.arange( N)*dx
    f_int  = dx*( f_x(a_xi)).sum()
    return f_int

def mean_value( midpoint, x0, xn):
    return (1 / ( xn - x0))*midpoint
    
midpoint_a = midpoint( f_x_a, 0, np.pi, 1000)
mean_value_a = mean_value( midpoint_a, 0, np.pi)
exact_solution_a = ( 1 / np.pi)*2

midpoint_b = midpoint( f_x_b, 0, 1, 1000)
mean_value_b = mean_value( midpoint_b, 0, 1)
exact_solution_b = np.e - 1

print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
print 'Exact Mean Pt. A = ', exact_solution_a
print 'Approximation Pt. A = ', mean_value_a
print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
print 'Exact Mean Pt. B = ', exact_solution_b
print 'Approximation Pt. B = ', mean_value_b