# -*- coding: utf-8 -*-
#Python 2.7, Anaconda 2
"""
Created on Sat Apr 13 01:16:22 2019

@author: bruno

This is a program to find the area of a rectangle and a triangle
using two functions to do so and then it prints out the result in one line.

"""

a = input("Enter the height of the rectangle") #The height of the rectangle
b = input("Enter the base, will be used for the rectangle and triangle") #base of triangle and rectangle
hb = input("Enter the height of the triangle") #The height of the triangle

#a function to find the area of a rectangle
def rectArea(height,base):
    return height * base #returns the area

#Finds the area of a triangle
def triangleArea(height,base):
    return 0.5 * height * base #returns the area

print "The area of the rectangle is %3.2f and the area of the triangle is %3.2f" % (rectArea(a,b), triangleArea(hb,b))


