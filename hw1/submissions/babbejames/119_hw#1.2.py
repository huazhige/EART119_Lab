#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author: jtbabbe
Find area of an irregular polygon given vertices
"""
import numpy as np

#=============================
#            Array def
#============================= 

xi = np.zeros(5)
yi = np.zeros(5)

xi[0] = 1
xi[1] = 3
xi[2] = 4
xi[3] = 3.5
xi[4] = 2

yi[0] = 1
yi[1] = 1
yi[2] = 2
yi[3] = 5
yi[4] = 4 

#===================================
#           function def
#==================================

# for loop method
def area_polygon( xi, yi):
    sum_poly = 0
    for i in range(5):
        sum_poly += ((xi[i-1]*yi[i])-(yi[i-1]*xi[i]))
    print 'Area of the parcel is', .5 * sum_poly, 'units (for-loop method)'
        
# vector method 
def area_polygon_vec( xi, yi):
    area = .5*(((xi[0]*yi[1])+(xi[1]*yi[2])+(xi[2]*yi[3])+(xi[3]*yi[4])+(xi[4]*yi[0]))-((yi[0]*xi[1])+(yi[1]*xi[2])+(yi[2]*xi[3])+(yi[3]*xi[4])+(yi[4]*xi[0])))
    print 'Area of the parcel is', area, 'units (vector method)'


#=====================================
#           1: for loop method
#=====================================

area_polygon( xi, yi)
        
#======================================
#           2: vector method
#=====================================

area_polygon_vec( xi, yi)

