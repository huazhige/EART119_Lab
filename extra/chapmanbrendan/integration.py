# -*- coding: utf-8 -*-
"""
Created on Thu May 16 18:19:55 2019

@author: blchapma
"""
import numpy as np
import matplotlib as plt
from math import e



def f(x):  return 3*(x**2)*(e**(x**3))  # This is the function we will integrate.
'''
A function can be as simple as the one-liner above.  By the way, we will be
mixing text and executable code freely in this tutorial.  The triple quotes
make the text a "multi-line string".  At the beginning of a module or function,
these are the "docstrings" we will use later in automated documentation and
testing.  Elsewhere, they are just ignored by the Python iterpreter.

You should be reading this file in IDLE (Python's Integrated Development
Environment.  Many text editors won't display all the colors that make
readability so nice.
~'''


'''
The first thing you may notice about Python, is that there are no brackets and
semicolons or other punctuation to define statements and code blocks.  Thus
"program structure" is established by indentation.  While this may seem like a
bad idea to anyone who has not tried Python, it actually is better for teaching
(and for experienced programmers who might make simple blunders).  The
interpreter catches indentation errors, and won't let the student continue with
a subtle eror because a curly bracket is out of place.  Teachers no longer have
to nag students about proper style.

Notes on the code above:

1) Python has a very flexible argument-passing syntax.  If you include a
"default value" with a parameter (nbins=10), that makes it a "keyword"
parameter.  Keyword parameters are optional in a call to the function.

2) Python variables have no type.  Parameters a, b and f above are expected to
be two floats and a function.  While type declarations would catch some errors,
Python expects the programmer write explicit and complete checks in those
situations where defensive programming is important (like user input).

The checks above do a lot more than just type checking.  They also serve as
documentation. Students will learn early about good programming practices, if
teachers include some bad inputs in their automated test cases.  On the other
hand, if the emphasis is on learning algorithms, not programming, these tests
can be left out.  Python allows that flexibility.
~'''

def integMid(a, b, f, nbins=10):
    '''Return the integral from a to b of function f using the midpoint rule

    >>> integMid(0, 1, f, 4)
    0.828125
    '''
    h = float(b-a)/nbins
    assert h > 0
    assert type(nbins) == int
    
    sum = 0.0
    x = a + h/2                  # first midpoint
    while (x < b):
        sum += h * f(x)
        x += h

    return sum

def integTrap(a, b, f, nbins=10):
    '''Return the integral from a to b of function f using trapezoidal rule

    >>> integTrap(0, 1, f, 4)
    0.84375
    '''
    h = float(b-a)/nbins
    assert h > 0
    assert type(nbins) == int
    
    sum = (h/2) * (f(a) + f(b))  # endpoints are special
    for n in range(1, nbins):    # [1, 2, ... nbins-1]
        sum += h * f(a + n*h)
    
    return sum
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

"Conversion to polar coord"
def cart2pol(x, y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return(rho, phi)