# -*- coding: utf-8 -*-
"""

        write a program that computes the area of a rectangle and a triangle
        inputs:
            b     = length
            c     = width
            h     = height
            b_tri = base length

"""
#takes user input for b and c
b = float(raw_input("Enter length of rectangle."))
c = float(raw_input("Enter width of rectangle."))

#find the area of a rectangle using A=bc
def rect_area(b,c):
    A = b*c
    return (A)
print (rect_area(b,c)) 

#takes user input for h and b_tri
h = float(raw_input("Enter height of triangle."))
b_tri = float(raw_input("Enter base length of triangle."))

#find the area of a triangle using A=0.5*hb
def tri_area(h,b_tri):
    A = 0.5*h*b_tri
    return (A)
print (tri_area(h,b_tri)) 