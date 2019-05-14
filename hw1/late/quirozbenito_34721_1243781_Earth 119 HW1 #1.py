# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 17:37:56 2019
Earth 119 HW1 Problem #1
@author: Benny Quiroz
"""
#This function gives the area of either a rectangle or triangle,
#which must be specified in the argument. 
#The function simply checks if it's a rectangle or triangle and applies the,
#appropriate formula to the base and height arguments. 
def area(base, height, shape):
    if shape is "rectangle" or shape is "Rectangle":
        return base*height
    elif shape is "triangle" or shape is "Triangle":
        return .5*base*height
    else:
        return "Please specify whether you'd like the area of a rectangle or a triangle."
    
#Test code for area()
print area(2, 10, "rectangle")
print area(3.45, 7.99, "Rectangle")
print area(3, 7, "triangle")
print area(4.95, 6.83, "Triangle")
print area(2, 5, "pentagon")
