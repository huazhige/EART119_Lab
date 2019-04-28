#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 19:17:19 2019

@author: charity
"""

def triangle(a, b): 

    return (0.5 * a * b) 


def perimeterRectangle(a, b): 

    return (2 * (a + b)) 

def areaRectangle(a, b):
    
    return (a * b)

  
# Driver function 

a = 5; 

b = 6; 

print ("Area = ", areaRectangle(a, b)) 

print ("Perimeter = ", perimeterRectangle(a, b))