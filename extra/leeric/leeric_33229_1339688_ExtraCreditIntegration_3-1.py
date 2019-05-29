# -*- coding: utf-8 -*-
"""
Created on Sat May 18 14:37:19 2019
Problem 3 Extra Credit Integration
Monte Carlo Integration
@author: eric_
"""
import numpy as np


xmin, xmax = -2, 2
ymin, ymax = -2, 2

xmin2, xmax2 = 0-1, 2+1
ymin2, ymax2 = 0-1, 1.5+1
n = 3000 # number of random points
#================================================
#          functions
#================================================
def function_1( x, y):
    return np.sqrt(x**2 + y**2)

def domain_1( x, y):
    " domain: circle with a radius of 2 centered at the origin"
    r_value = -1
    if np.sqrt(x**2 + y**2) <= 2:
        r_value = 1
    return r_value

def function_2( x, y):
    return x*y**2

def domain_2(x, y):
    "domain: rectangle with dimensions 0 < x < 2 and 0 < y < 1.5"
    r_value2 = -1
    if 0 <= x <= 2 and 0 <= y <= 1.5:
        r_value2 = 1
    return r_value2

#generate random values within a rectangle with dimensions x and y
a_xran = np.random.uniform( xmin, xmax, n) 
a_yran = np.random.uniform( ymin, ymax, n)
mean_value1 = 0
num_inside = 0.0 # number of points with x,y; g(x,y) >= 0
for i in range( n): # x loop
    for j in range( n): # y loop
        if domain_1( a_xran[i], a_yran[j]) >= 0:
            num_inside += 1 
            mean_value1 += function_1( a_xran[i], a_yran[j])
mean_value1 /= num_inside #Average value of function inside circle
# area of domain is approximate by q*Ar
q = num_inside/(n*n)
Area_rectangle = (xmax - xmin)*(ymax - ymin)
Area_omega = q*Area_rectangle
integral_1 = Area_omega*mean_value1

print("no. of random points", n, 'num integral', integral_1)
print("Analytical Solution: ", (16*np.pi)/3)
print()

#===============================================================
#       SECOND FUNCTION
#===============================================================

a_xran2 = np.random.uniform( xmin2 , xmax2 , n) 
a_yran2 = np.random.uniform( ymin2 , ymax2 , n)
mean_value2 = 0
num_inside2 = 0.0 # number of points with x,y; g(x,y) >= 0
for i in range( n): # x loop
    for j in range( n): # y loop
        if domain_2( a_xran2[i], a_yran2[j]) >= 0:
            num_inside2 += 1 
            mean_value2 += function_2( a_xran2[i], a_yran2[j])
mean_value2 /= num_inside2
q2 = num_inside2/(n*n)
Area_rectangle2 = (xmax2 - xmin2 )*(ymax2 - ymin2)
Area_omega2 = q2*Area_rectangle2
integral_2 = Area_omega2*mean_value2
print("Second Function")
print("no. of random points", n, "num integral", integral_2)
print("Analytical Solution: ", 2.25)



































