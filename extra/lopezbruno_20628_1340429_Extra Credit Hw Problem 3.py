# -*- coding: utf-8 -*-
"""
Created on Fri May 17 16:30:28 2019

@author: bruno
"""

import numpy as np



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
    f_Aom       = num_inside/float(n**2) * (xmax-xmin)*(ymax-ymin)
    return f_Aom*f_fct_mean

def fx1(x,y):
    return x * (y **2)

#Uses th boundary omega to ifnd the g(x) function
def gx1(x,y):
    return 3 - (x * y)

def fx2(x,y,r = 4):
    return (r * np.cos(x)**2 + r * np.sin(y) **2) ** 0.5

def gx2(x,y, r = 4):
    return 4 - (r * np.cos(x)**2 + r * np.sin(y) **2) ** 0.5
    
    

#The x and y min boundary
theMin = 0
#The x max boundary
xmax1 = 2
xmax2 = 2 
#The Y max boundary
ymax1 = 1.5
ymax2 = 2

print ("The area using the monte carlo method of the first function is %1.5f") % monteCarlo(fx1,gx1,theMin,xmax1,theMin,ymax1,1000)
print ("The area of the second function using monte carlo is %1.5f") % monteCarlo(fx2, gx2, theMin , xmax2 ,theMin, ymax2,1000)    