# Allison Swart
# Astro/Earth 119 Homework #1
# April 14, 2019

#anaconda2/python2.7

import numpy as np

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#            Problem 2
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PART ONE--As a for loop

def polygon_area( X, Y, n):
    area = 0.0
    m = n - 1
    i = 1
    for i in range( 0, n):
        area += (X[m] + X[i])*(Y[m] - Y[i])
        m = 1
    return int( abs( area / 2))

X = ( 1, 3, 4, 3.5, 2)      #x-coordinates
Y = ( 1, 1, 2, 5, 4)        #y-coordinates
n = len(X)                  #loop parameter

print 'polygon area = ', polygon_area( X, Y, n)

# PART TWO--Vector notation

x_values = np.array( [1, 3, 4, 3.5, 2])
y_values = np.array([1, 1, 2, 5, 4])

    
print 'area vectorized = ', (np.dot( x_values, y_values) / 2)