# -*- coding: utf-8 -*-
"""
Code by Jason Minera
using python 2.7
due 4/14/19

Question:
Historically, an important mathematical problem was to find the area of an 
irregular polygon, which is a key question for land usage and taxation. 
We will come back to computing the area of irregular polygons in spherical 
coordinates. For now, consider a polygon with five vertices in Cartesian
coordinates: (1,1); (3,1); (4,2); (3.5, 5); (2,4). Write a function to 
compute the area of this polygon. Interestingly the area can simply be 
computed from the know vertices using the following equation: 
A=	½|(x1y2	+	x2y3	+	…	xn-1yn	+	xny1)	-	(y1x2	+	y2x3	+	…	+	yn-1xn	+	ynx1)|	
Your function will take two vectors ( x i and y i) as input and return the 
area of the polygon A. As test cases, you can use the functions for the area 
of a rectangle with (0,0); (2,0); (2,3) and triangle with (3,1); (2,3) and 
(0,1) and then compute the area of the fivesided polygon. Write to different 
functions: 1) area_polygon.py – which solves the above equation within a for 
loop and 2) area_polyon_vec.py – which solve the equation using vector notation
"""

import numpy as np #calling the numpy package as np
import matplotlib.pyplot as plt #calling the matplotlib package to be able to plot as plt

x = np.array([1., 3., 4., 3.5, 2.]) # array of the x axis given to us
y = np.array([1., 1., 2., 5., 4.])  # array of the y axis given to us

# this is to show the user the array we are working with
print('xi', x)
print('yi', y)

plt.plot(x, y, marker = 'o' , linestyle = 'none', color = 'black') #plotting the x array and y array
plt.xlim(0,7) # This is plotting the axis for x from 0 to 7
plt.ylim(0,7) # This is plotting the axis for y from 0 to 7

area_polygon = 0 # variable stating

for i in np.arange( 0, 5, 1):
    #print x[i-1] , y[i], y[i-1], x[i] (i used this for i can see the numbers in a row and calculate it by hand to see if im getting the right area)
    area_polygon += 0.5*((x[i-1]*y[i]) - (y[i-1]*x[i]))
    
    #print('area = %.1f' %area_polygon)    #This was giving me multiple areas until we got the area
    
print('The area of the polygon calculated by the for loop is %.1f' %area_polygon)

#sumation of the array by vector notation
area_polygon_vec = 0.5*(x[0]*y[1]-y[0]*x[1]) + 0.5*(x[1]*y[2]-y[1]*x[2]) + 0.5*(x[2]*y[3]-y[2]*x[3]) + 0.5*(x[3]*y[4]-y[3]*x[4]) + 0.5*(x[4]*y[0]-y[4]*x[0]) 

print ('The area of the polygon calculated by vector notation %.1f' %area_polygon_vec)



