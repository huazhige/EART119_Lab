import numpy as np
import matplotlib.pyplot as plt
import integrate_utils as utils


def fct_t(t):
    return 3*t**2 * (np.e)**t**3

t_trap = utils.trapezoidal(fct_t, 0, 1, 1000)

t_mid  = utils.midpoint(fct_t, 0, 1, 1000)

print('Trapezoidal: ', t_trap)

print('Midpoint: ', t_mid)


#def trapezoidal(  fct_t, t0, tn, N):
#    """
#            Composite Trapezoidal Method, eq. 3.17 page 60 in Linge & Langtangen
#    :param fct_x:  - function whose integral is in question
#    :param x1:     - integration bounds
#    :param x2:     - integration bounds
#    :param N:      - number of trapezoids, chose high number for high accuracy
#    :return:   - integral of fct_x between x0 and xn
#    """
#    t0 = 0
#    tn = 1
#    N = 1000
#    dt = float(tn-t0)/N
#    # compute intergral: eq. 3.17 page 60 in Linge & Langtangen
#    f_Int  = 0.5*(fct_t( t0) + fct_t( tn)) + ( fct_t( t0+dt*np.arange(1, N, 1))).sum()
#    # as a for loop
#    f_Int  = 0.5*(fct_t( t0) + fct_t( tn))
#    for i in range( 1, N):
#        f_Int += fct_t( t0 + i*dt)
#    print( f_Int*dt)
#    return dt*f_Int
#def midpoint( fct_t, t0, tn, N):
#    """
#            Composite Midpoint method, eq. 3.21 page 66 in Linge & Langtangen
#    :param fct_x:  - function whose integral is in question
#    :param x1:     - integration bounds
#    :param x2:     - integration bounds
#    :param N:      - number of trapezoids, chose high number for high accuracy
#    :return:   - integral of fct_x between x0 and xn
#    """
#    dt     = float( tn-t0)/N
#    a_ti   = t0 + 0.5*dt + np.arange( N)*dt
#    f_int  = dt*( fct_t(a_ti)).sum()
#    return f_int