# -*- coding: utf-8 -*-
'''
Cesar Laguna
Python 3.6
'''
import numpy as np
'''
# 2
Area of polygon in carestian coordiantes  
'''

Coord = [[1., 1.], [3., 1.], [4., 2.], [3.5, 5.], [2., 4.]]
n = len(Coord)
def PolyArea(Coord):
    area1, area2 = 0, 0   #want the area to start off as zero and grow with our inputs/ function
    for i in range(n):
        j = (i + 1) % n
        area1 += Coord[i][0] * Coord[j][1]   #calculates the first half of finding the area of the polygon
        area2 -= Coord[j][0] * Coord[i][1]   #calculates the second half of finding the area of the polygon
    area = abs(area1+ area2)/ 2.0   #its (area1 + area2) and not (area1 - area) because area2 is defined as negative numbers "area -="
    return (area)
print('Area of the Polygon', PolyArea(Coord))
'''
# 2 
Vectorized Notation for area of a polygon
'''
x = (1, 3, 4, 3.5, 2)
y = (1, 1, 2, 5, 4)
def PolyAreaV(x, y):
    return 0.5*np.abs(np.dot(x,np.roll(y,1))-np.dot(y,np.roll(x,1)))  #is going to take the dot product of correspoing values of x and y 
                                                                      #until it has gone thru all the numbers in the list
print ('Area of Polygon, Vectors', PolyAreaV(x,y))