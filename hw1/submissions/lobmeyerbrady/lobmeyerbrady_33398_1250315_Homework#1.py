# -*- coding: utf-8 -*-
"""
Brady Lobmeyer 4/13/2019
Find the area of a rectangle and triangle
Area of rectangle A=bc
Area of triangle A=.5hb
"""

#area of rectangle m^2
def A(t): #defining a function for Area of rectangle
    b0 = 5
    c0 = 7
    return (b0*t)*(c0*t) #('base times height')

time = 1        #('just pick a point in time')
print A(time)
time = 20       #('just pick a point in time')
print A(time)

#area of triangle m^2
def Atri(t): #defining a function for Area of triangle 
    hb = 5 #('dimensions of triangle')
    h  = 10
    return (.5*h*t)*(hb*t) #('base times height over two')

time = 1        #('just pick a point in time')
print Atri(time)
time = 20       #('just pick a point in time')
print Atri(time)

