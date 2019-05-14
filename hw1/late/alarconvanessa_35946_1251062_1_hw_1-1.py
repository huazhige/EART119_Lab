# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 17:59:40 2019

Homework problem set #1
anaconda/python 3.7

@author: Nessa
"""

"""
PROBLEM 1
Computes the area of a rectangle and the area of a triangle
"""
#//////////////////////////////////////////////////////////////////////////////
#                           Variables
#//////////////////////////////////////////////////////////////////////////////

b = int((input ("Rectangle side length b =")))
c = int((input ("Rectangle side length c =")))

h_b = int((input ("Triangle side length h_b =")))
b_tri = int((input ("Triangle side length b =")))



#//////////////////////////////////////////////////////////////////////////////
#                        calculations
#//////////////////////////////////////////////////////////////////////////////

#Area of rectangle computation
def RectArea(b,c):
    return print (b*c)

# Area of triangle computation
def TriArea(h_b,b_tri):
    return print(0.5*h_b*b_tri)

print ("Area of Rectangle:")
RectArea(b,c)
print ("Area of Triangle: ")
TriArea(h_b, b_tri)


"""
PROBLEM 2

function to comput the area of an irregular polygon

"""



