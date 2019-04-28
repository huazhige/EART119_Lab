# -*- coding: utf-8 -*-
"""
author @jtbabbe
Write a function that computes the area of a rectangle A=bc.
Write a function that computes the area of a triangle A = 0.5*hb*b

"""

#=============================
#              variable meanings
#=============================

#               Rectangle
#b       = Width of Rectangle
#c       = Length of Rectangle

#               Triangle
#hb      =  Height of Triangle
#b       =  Width of Triangle


#===================================
#              function defs
#==================================

# rectangle function
def f_aR( b, c):
    areaR = float(b) * float(c)
    print'Area of the rectangle is :', areaR, ' units'
    
# traingle function
def f_aT( hb, b):
    areaT = .5 * float(hb) * float(b)
    print'Area of the triangle is :', areaT, ' units'

#=====================================
#               run functions
#=====================================

f_aR ( 10, 10)
f_aT ( 10, 10)





