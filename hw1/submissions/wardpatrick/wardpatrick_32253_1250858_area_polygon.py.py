# -*- coding: utf-8 -*-

"""
Question 2

Write a function to compute the area of a polygon with five vertices 
in Cartesian coordinates: (1,1); (3,1); (4,2); (3.5, 5); (2,4). 

A	=	½|(x1y2 +	x2y3 +	…	xn-1yn +	xny1)	- (y1x2 +	y2x3 +	…	+	yn-1xn +	ynx1)|

"""
import numpy as np

#===========================
#       Test Shapes
#===========================

## rectangle 
#pts = [[0,0], [2,0], [2,3], [0,3]]

## triangle 
#pts = [[3,1], [2,3], [0,1]]

#===========================
#       Polygon
#===========================

## irregular polygon
pts = [[1, 1], [3, 1], [4, 2], [3.5, 5], [2, 4]] 

#===========================
#       Calculation
#===========================

arr = np.array(pts)

area = 0
t1, t1n = 0, 0
t2, t2n = 0, 0
for i in range (1,len(pts)):
    xn   = arr[i,0]
    yn   = arr[i,1]
    xn_1 = arr[i-1,0]
    yn_1 = arr[i-1,1]
    x1   = arr[0, 0]
    y1   = arr[0, 1]
    xlst = arr[-1, 0]
    ylst = arr[-1,1]
    
    t1n += xn_1*yn
    t1 = t1n + xlst*y1
    
    t2n += yn_1*xn
    t2 = t2n + ylst*x1
    
area = .5*abs(t1-t2)

print ('Area:',area)
    
     
    
        