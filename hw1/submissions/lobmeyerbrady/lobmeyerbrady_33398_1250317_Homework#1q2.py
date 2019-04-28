# -*- coding: utf-8 -*-

"""
Brady Lobmeyer 4/14/2019
finding area of irregular polygon
Using both a for loop and vector notation

"""


a = (1., 2., 3., 3.5, 4.)
b = [1., 4., 1., 5., 2.]
for i in a:
    for j in b:
        A = [abs(((a[0]*b[1]+a[1]*b[2]+a[2]*b[3]+a[3]*b[4]+a[4]*b[0])*.5)-((b[0]*a[1]+b[1]*a[2]+b[2]*a[3]+b[3]*a[4]+b[4]*a[0])*.5))]
        
print A






