# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 19:46:39 2019
HW1 Problem #2
@author: Benny Quiroz
"""
import numpy as np

def area_polygon(xs, ys):
     #If statement is only to make sure the lengths of the point lists match.
    if len(xs) == len(ys):
        A = 0
        B = 0
        #Computes (x1y2 + ... + xny1)
        for i in range(-1, len(xs) - 1):
            A += xs[i]*ys[i+1]
        #Computes (y1x2 + .. + ynx1)
        for i in range(-1, len(ys) - 1):
            B += ys[i]*xs[i+1]
        C = abs(A-B)
        C = 0.5*C
        return C
    else:
        return "Your x's and y's are uneven!"
    
"""
So I wrote this function before I learned what the np.roll() function does.

Another thing to note about that formula in the problem is that the points
that you enter must be in the order of a loop around the shape. If you don't 
put them in in order the answer will be wrong. 
Wasted me a bunch of time so maybe put that in the problem next time. 

def area_polygon_vec(xs, ys):
    #Creating arrays that can be modified from the original arrays
    xs_mod = zeros(len(xs))
    ys_mod = zeros(len(ys))
    #If statement is only to make sure the lengths of the point lists match.
    if len(xs) == len(ys):
        #Each for loop moves each entry one forward and puts the first one at the end
        #The -1 starts it on the last element that way I don't have to store it in an unnecessary variable
        for i in range(-1, len(xs) - 1):
            xs_mod[i] = xs[i + 1]
        for i in range(-1, len(ys) -1):
            ys_mod[i] = ys[i + 1]
        #Now just applying the formula
        A = float(np.dot(xs, ys_mod))
        A = A - float(np.dot(ys, xs_mod))
        A = np.abs(A)
        A = 0.5*A
        return A        
    else:
        return "Your x's and y's are uneven!"
"""

def area_polygon_vec(xs, ys):
    #If statement is only to make sure the lengths of the point lists match.
    if len(xs) == len(ys):
        #Roll function just shifts the array over one
        A = np.dot(xs, np.roll(ys,1)) - np.dot(ys, np.roll(xs, 1))
        A = np.abs(A)
        A = 0.5*A
        return A        
    else:
        return "Your x's and y's are uneven!"
    
#Test code according to the problem.
x = [1,3,4,3.5,2]
y = [1,1,2,5,4]
print area_polygon(x, y)
print area_polygon_vec(x, y)

