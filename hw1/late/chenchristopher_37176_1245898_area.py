# -*- coding: utf-8 -*-
#python 2.7
"""
 - Computes the area of a rectangle or triangle
 - For rectangles, side lengths b and c are used
 - For triangles side length b and height hb are used
"""

#====================================================================================================
#functions to find the area of each shape
#====================================================================================================
def rect_area(b, c):
   return b * c

def tri_area(b, hb):
    return 0.5 * b * hb
    
#====================================================================================================
#user interface
#====================================================================================================
print("What shape would you like to find the area of?")
shape = raw_input('Type r for rectangle or t for triangle.')

if shape == "r":
    b = input('What is one of the side lengths?')
    c = input('What is the other side length?')
    print("The area is " + str(rect_area(b, c)) + " square units.")
elif shape == "t":
    b = input('What is the base length?')
    hb = input('What is the height?')
    print("The area is " + str(tri_area(b, hb)) + " square units.")
else:
    print("Invalid input")