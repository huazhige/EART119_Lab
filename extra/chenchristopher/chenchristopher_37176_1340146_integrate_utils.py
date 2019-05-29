# python2.7
"""
    - Integration modules includes:

     (1) - trapezoidal method
     (2) - midpoint method
     (3) - Monte Carlo Integration in omega for f(x,y)

"""

import numpy as np

def trapezoidal(  fct_x, x0, xn, N):
    """
            Composite Trapezoidal Method, eq. 3.17 page 60 in Linge & Langtangen
    :param fct_x:  - function whose integral is in question
    :param x1:     - integration bounds
    :param x2:     - integration bounds
    :param N:      - number of trapezoids, chose high number for high accuracy
    :return:   - integral of fct_x between x0 and xn
    """
    dx = float(xn-x0)/N
    # compute intergral: eq. 3.17 page 60 in Linge & Langtangen
    f_Int  = 0.5*(fct_x( x0) + fct_x( xn)) + ( fct_x( x0+dx*np.arange(1, N, 1))).sum()
    # # as a for loop
    # f_Int  = 0.5*(fct_x( x0) + fct_x( xn))
    # for i in range( 1, N):
    #     f_Int += fct_x( x0 + i*dx)
    # print( f_Int*dx)
    return dx*f_Int

def midpoint( fct_x, x0, xn, N):
    """
            Composite Midpoint method, eq. 3.21 page 66 in Linge & Langtangen
    :param fct_x:  - function whose integral is in question
    :param x1:     - integration bounds
    :param x2:     - integration bounds
    :param N:      - number of trapezoids, chose high number for high accuracy
    :return:   - integral of fct_x between x0 and xn
    """
    dx     = float( xn-x0)/N
    a_xi   = x0 + 0.5*dx + np.arange( N)*dx
    f_int  = dx*( fct_x(a_xi)).sum()
    return f_int


def monteCarlo( f_xy, g_xy, xmin, xmax, ymin, ymax, n):
    """
        - integrate fct f_xy over potential complex domain omega described by g(x,y)
          --> g(x,y) has to defined so that pointes within domain follow:
              g(x,y) >= 0
        (1) randomly draw n points in x and y,
        (2) find points in domain g(x,y), which is embeded in a rectangle
            wiht Ar and bounded by (xmin, xmax, ymin, ymax)
        (3) compute mean function values of points inside of domain omega
        (4) compute area of domain omega from fraction of points and Ar
        (5) Int(f_xy dxdy) = f_mean*A_omega
    :param f_xy:  - function that should be integrated
    :param g_xy:  - function that defines integration domain
                    g >= 0
    g_xy is embeded in rectangle with:
    :param  - xmin, xmax, ymin, ymax
    :param n:  - number of random points in x and y, total no. = n**2

    :return: - float( ) - definite integral of f_xy
    """
    # create n random points in x and y
    a_xran = np.random.uniform( xmin, xmax, n)
    a_yran = np.random.uniform( ymin, ymax, n)
    ########### solve using for loop: A_om, f_mean###########
    f_fct_mean = 0
    num_inside = 0 # number of points with x,y; g(x,y) >= 0
    for i in range( n): # x loop
        for j in range( n): # y loop
            if g_xy( a_xran[i], a_yran[j]) >= 0:
                num_inside += 1
                f_fct_mean += f_xy( a_xran[i], a_yran[j])
    f_fct_mean /= num_inside
    # ############ vectorized version ###########
    # m_xran, m_yran = np.meshgrid( a_xran, a_yran)
    # sel = g_xy( m_xran, m_yran) >= 0
    # num_inside = sel.sum()
    # print( f_fct_mean)
    # f_fct_mean = np.mean( f_xy( m_xran[sel], m_yran[sel]))
    # print( f_fct_mean)

    # last two lines are the same for loop and vectorized solutions:
    # area of domain is approximate by q*Ar, where q is fraction of points in domain, and Ar is area of rectangle
    f_Aom       = num_inside/float(n**2) * (xmax-xmin)*(ymax-ymin)
    return f_Aom*f_fct_mean

def monteCarlo_vec( f_xy, g_xy, xmin, xmax, ymin, ymax, n):
    """
        - integrate fct f_xy over potential complex domain omega described by g(x,y)
          --> g(x,y) has to defined so that pointes within domain follow:
              g(x,y) >= 0
        (1) randomly draw n points in x and y,
        (2) find points in domain g(x,y), which is embeded in a rectangle
            wiht Ar and bounded by (xmin, xmax, ymin, ymax)
        (3) compute mean function values of points inside of domain omega
        (4) compute area of domain omega from fraction of points and Ar
        (5) Int(f_xy dxdy) = f_mean*A_omega
    :param f_xy:  - function that should be integrated
    :param g_xy:  - function that defines integration domain
                    g >= 0
    g_xy is embeded in rectangle with:
    :param  - xmin, xmax, ymin, ymax
    :param n:  - number of random points in x and y, total no. = n**2

    :return: - float( ) - definite integral of f_xy
    """
    # create n random points in x and y
    a_xran = np.random.uniform( xmin, xmax, n)
    a_yran = np.random.uniform( ymin, ymax, n)
    ############ vectorized version ###########
    m_xran, m_yran = np.meshgrid( a_xran, a_yran)
    sel = g_xy( m_xran, m_yran) >= 0
    num_inside = sel.sum()
    f_fct_mean = np.mean( f_xy( m_xran[sel], m_yran[sel]))
    # last two lines are the same for loop and vectorized solutions:
    # area of domain is approximate by q*Ar, where q is fraction of points in domain, and Ar is area of rectangle
    f_Aom       = num_inside/float(n**2) * (xmax-xmin)*(ymax-ymin)
    return f_Aom*f_fct_mean

