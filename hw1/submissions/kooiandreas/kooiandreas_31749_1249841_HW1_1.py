#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IDE: Spyder
Andreas Kooi
April 14, 2019

HW1.1
Write a program that computes the area of a rectangle (A=bc) and the area of a triangle
(A = 0.5*hbb). The input of your function will be b and c for the rectangle and hb and b
for the triangle
"""

#=============================
#       Functions
#=============================

def area_rect( b,c ):
    return( b*c )

def area_tri( h_b, b ):
    return( 0.5*h_b*b )




#=============================
#       Parameters
#=============================


b = float(input('What is the length of the rectangle? '))
c = float(input('what is the height of the rectangle? '))


b = float(input('What is the base length of the triangle? '))
h_b = float(input('What is the height of the triangle? '))





#=============================
#       Computations and Display
#=============================

area_rect = area_rect(b,c)
area_tri = area_tri(h_b,b)

print('The area of the rectangle is %.2f and the area of the triangle is %.2f'%(area_rect,area_tri))