# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 16:43:29 2019

@author: lopez
"""

#################################### Problem No.2##############################
"""
Problem#2

Computing the area of a polygon
"""
corners = [(1,1), (3,1), (4,2), (3.5,5), (2,4)]   # x and y Cartesian Coordinates  
def PolygonArea(corners):
        n= len(corners)                           #Lenght of Coordinates 
        area1, area2= 0, 0                        # Starting values of areas 
        for i in range(n):
            j = (i+1) % n
            area1 += corners[i][0] * corners[j][1]
            area2 -= corners[j][0] * corners[i][1]
        area = abs(area1+area2)/2
        return area
print('area of polygon', PolygonArea(corners))
