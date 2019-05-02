#python2.7
"""
    -  compute that cross-over point between two discrete fct. f(x) and g(x)
"""
import numpy as np
import scipy.optimize
import matplotlib.pyplot as plt

#--------------my modules----------------------------
import Optimize.opt_utils as opt_utils

#===================================================================================
#                                define fct.
#===================================================================================
def f_t( t, c, t0):
    return c*(t - t0)**2

def g_t( t, A, t0):
    return A*t + t0

def f_g_t( t, par): #t, A, c, t0):
    """
    :param t:
    :param par: A, c, t0
    :return:
    """
    A, c, t0 = par[0], par[1], par[2]
    return f_t( t, c, t0) - g_t( t, A, t0)

def f_g_t_scipy( t,  A, c, t0):
    """
    :param t:
    :param par: A, c, t0
    :return:
    """
    return f_t( t, c, t0) - g_t( t, A, t0)

def my_Secant( fct, par, x0, x1, verbose = False, **kwargs):
    """
    :param fct:     - find root of this fct. closes to x0
    :param par:     - parameters needed for function call: fct( x, par)
    :param dfct_dt: - derivatice of fct
    :param x0, x1:  - interval for first secant estimate, with x0 close to root
    kwargs:
        :param Nit:       - number of iterations, default = 20
        :param tol:     - tolerance, default = 1e-4

              x_n+1 = (x_n - f(x_n))*[( x_n - x_n-1) / (f(x_n) - f(x_n-1))]
        with: x_n+1 = x2
              x_n   = x1
              x_n-1 = x0
    :return: f_r0 - root between x0 and x1
    """
    N   = 20
    tol = 1e-4
    if 'tol' in kwargs.keys() and kwargs['tol'] is not None:
        tol = kwargs['tol']
    if 'Nit' in kwargs.keys() and kwargs['Nit'] is not None:
        N = kwargs['Nit']
    x0 = float( x0)
    x1 = float( x1)
    i  = 0
    while abs( fct( x1, par)) > tol and i < N:
        df_dt  = float(fct( x1,par)-fct( x0,par))/(x1-x0)
        x2 = x1 - fct( x1, par)/df_dt
        if verbose == True:
            print(  i, 'fct-value: ', round( abs( fct( x1, par)),4), 'x: ', round( x2,4))
        # update variables at new step
        x0 = x1
        x1 = x2
        i += 1
    if abs( fct( x1, par)) > tol: # no solution found
        return None
    else:
        return float( x2)
#===================================================================================
#                                params
#===================================================================================
iN = 1000
tmin, tmax = -10, 10
t0 = 2.5
c  = 1.1
A  = 5
# secant method initial interval:
f_root0, f_root1 = 2, 3


eps= 1e-1
testPlot = True

a_t = np.linspace( tmin, tmax, iN)

#===================================================================================
#                             find cross-over point
#===================================================================================
## compute fct values
a_ft  = f_t(  a_t, c, t0)
a_gt  = g_t(  a_t, A, t0)

#f_Nw_x0 = opt_utils.my_Newton( f_g_t, dfdx, x0)
f_Sc_x0  = my_Secant( f_g_t, [A, c, t0], f_root0, f_root1)
print( 'my-secant: t', f_Sc_x0, 'f_t', f_t( f_Sc_x0, c, t0),'g_t', g_t( f_Sc_x0, A, t0) )
f_t0_opt = scipy.optimize.newton( f_g_t_scipy, f_root0, args = (A,c,t0 ))
print( 'scipy: t', f_t0_opt, 'f_t', f_t( f_t0_opt, c, t0),'g_t', g_t( f_t0_opt, A, t0) )

a_df_g  = a_ft - a_gt
## find all cross-over points
sel = abs(a_df_g) < eps
print 'all cross-over points (grid search):, ',a_t[sel], a_ft[sel]


## test plot
if testPlot == True:
    plt.figure(1)
    plt.subplot( 211)
    plt.plot( a_t, f_t( a_t, c, t0), 'o', mec = 'r', ms = 2, mfc = 'none', label = 'f(t)')
    plt.plot( a_t, g_t( a_t, A, t0), 'o',     mec = 'b', ms = 2, mfc = 'none',  label = 'g(t)')
    plt.xlim( tmin, tmax)

    plt.subplot( 212 )
    plt.plot( [tmin, tmax], [0,0], 'k--')
    plt.plot( a_t, abs(a_df_g),  'o', mec = 'k', ms = 2, mfc = 'none', label = '|f - g|')
    plt.plot( [f_t0_opt], [ 0 ], 'r*', ms = 10)
    plt.xlabel( 't')
    plt.ylabel( 'Error Function')
    plt.xlim( tmin, tmax)
    #plt.ylim( -2, 10)

    plt.legend()
    plt.show()