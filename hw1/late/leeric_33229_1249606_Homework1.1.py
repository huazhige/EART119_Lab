# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 16:58:22 2019

@author: eric_
"""
#Problem 1
print("Compute the area of rectangle with side lengths b & c")
b = input("Value of b = ") #prompting user for side lengths with the input command
b2 = int(b) #changing the type to an integer
c = input("Value of c = ")
c2 = int(c)
Area_of_rectangle = b2*c2 #Computing the area of the rectangle

print("Area of the rectangle = ", Area_of_rectangle) #displaying the area of the rectangle

print("Now, compute the area of triangle with side lengths hb & b")
hb = input("Value of hb = ")
hb2 = int(hb)
Area_of_triangle = 0.5*hb2*b2
print("Area of the triangle = ", Area_of_triangle) #Displaying area of triangle

#Problem 2