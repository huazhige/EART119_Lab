#!Python2.7
"""Find the b value that gives the area of a rectangle a*b closest to the area of a circle pi*r^2."""

#import
import numpy as np

#inputs
a=1.5
r=12.6


def Maximum_b(a, r):
    def Area_of_circle(r):
        area = np.pi*r**2 #equation for the area of a circle
        return area
    def Area_of_rectangle(a, b):
        area = a*b #equation for area of a rectangle
        return area
    b = 0
    while Area_of_rectangle(a, b) < Area_of_circle(r):
        b = b + 0.5 #0.5 is the increment value
    return b - 0.5
print(Maximum_b(a,r))

def check_answer(a,r): #from algebraic solution
    b = np.pi*r**2/a
    return b
print (check_answer(a,r))
