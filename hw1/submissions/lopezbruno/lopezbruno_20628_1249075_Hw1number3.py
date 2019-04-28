# -*- coding: utf-8 -*-
#Python 2.7, Anaconda 2
"""
Created on Sat Apr 13 17:04:51 2019

@author: bruno

Two different programs to find the area of a polygon, given two vectors(xi,yi)
One of the methods will use a for loop, the other will use vectorization

"""

import numpy as np

# The X axis of the array
xi = np.array([1,3,4,3.5,2])
# The Y axis of the array
yi = np.array([1,1,2,5,4])
 


def areaForLoops(xi,yi):
    
    a = 0 # a placeholder, will contain (x0y1 + x1y2 + ... x(n-1)yn + xny1)
    b = 0  # a placeholder, will contain (y0x1 + y1x2 + ... y(n-1)xn + ynx1)
    i = 0 #Index counter for finding a
    j = 0 #Index counter for finding b
    
    #Finds the value of a using (x0y1 + x1y2 + ... x(n-1)yn + xny1)
    for i in range(0,len(xi) - 1):
        a += (xi[i] * yi[i+1])
        i += 1
    
    #This is to find the last term, the xny1 term
    a += xi[-1] * yi[0]
    
    #Finds the value of B using(y0x1 + y1x2 + ... y(n-1)xn + ynx1)
    for j in range(0,len(yi) - 1):
         b += (yi[j] * xi[j+1])
         j += 1
    
    #This is to find the last term, the ynx1 term    
    b += yi[-1] * xi[0]
         
     #returns the desired equation    
    return 0.5 * (a-b)

print "The area of the polygon using a for loop is: %1.2f" % areaForLoops(xi,yi)

""" 
 The polygon equation is (1/2) * ((xoy1 + x1y2 +... x(n-1)y(n)) + x(n)y0)
 ((yox1 + y1x2 +... y(n-1)x(n)) + y(n)x0)
    
 I will refer to ((xoy1 + x1y2 +... x(n-1)y(n)) + x(n)y0) as a
 and ((yox1 + y1x2 +... y(n-1)x(n)) + y(n)x0) as b
"""
def vectorArea(xi,yi):
    
    z = xi[:-1] #This is the x component of a, excluding the last element
    yz = yi[1:] # This is the y component of a, excluding the first element
    p = xi[1:] # This is the x component of b, excluding the first element
    o = yi[:-1] # This is the y component of b, excluding the last element
    x = np.dot(z,yz)# computes a, except the last term
    y = np.dot(o, p)# computes b, except the last term
    
    x += xi[-1]*yi[0]# adds the last term, the x(n)y0 term to x
    y += yi[-1]*xi[0]# adds the last term, the y(n)xo term to y
    
    return 0.5 * (x - y) #returns the full equation

print "The area of the polygon using vectorization is: %1.2f" % vectorArea(xi,yi)
