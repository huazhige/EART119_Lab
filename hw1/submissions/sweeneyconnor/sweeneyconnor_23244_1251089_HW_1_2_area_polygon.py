# -*- coding: utf-8 -*-
"""
HW 1 Q2

Historically, an important mathematical problem was to find the area of an irregular
polygon, which is a key question for land usage and taxation. We will come back to
computing the area of irregular polygons in spherical coordinates. For now, consider a
polygon with five vertices in Cartesian coordinates: (1,1); (3,1); (4,2); (3.5, 5); (2,4).
Write a function to compute the area of this polygon. Interestingly the area can simply
be computed from the know vertices using the following equation:
A	=	½|(x1y2 +	x2y3 +	…	xn-1yn +	xny1)	- (y1x2 +	y2x3 +	…	+	yn-1xn +	ynx1)|
Your function will take two vectors (xi and yi) as input and return the area of the
polygon A. As test cases, you can use the functions for the area of a rectangle with (0,0);
(2,0); (2,3) and triangle with (3,1); (2,3) and (0,1) and then compute the area of the fivesided polygon. Write to different functions: 1) area_polygon.py – which solves the
above equation within a for loop and 2) area_polyon_vec.py – which solve the equation
using vector notation.
"""
# Test with given triangle
x = [ 3, 2, 0, 3]
y = [ 1, 3, 1, 1]



for i in range(0, 3):
    A =   x[i]*y[i +1] - y[i]*x[i +1]
    
print "The Area of the (test)triangle is:", 0.5*abs(A)
    
    
# Area of 5-sided polygon using for loop
x = [ 1, 3, 4, 3.5, 2, 1]   #x coordinates; looping back to x[0]
y = [ 1, 1, 2, 5, 4, 1 ]    #y coordinates; ^^^^^^^^^^^^^^ y[0]

A = 0
for i in range(0, 5):
    A +=  x[i]*y[i +1] - y[i]*x[i +1]
    
print "The Area of the polygon is:", 0.5*abs(A) 