"""
Hw.1 Problem 3 for Earth-119
Calculating the area of a rectangle of side 'a' so that its area
is not bigger than a circle of radius 'R'
"""
import numpy as np

# constants ============================
R = 12.6
a = 1.5
b = 300
# equations=============================
A_circle = (np.pi)*(R**2)
A_rect = a * b
# a * b < A_circle, b < (A_circle)/a
# we want to find b such that A_rectangle is as close as possible to A_circle
# calculations =========================

while b+1 < (A_circle)/a :
    b += 1
print("b = %i"%b )
print("area of rectangle = %2f"%(b * a))
print("area of circle = %2f"%A_circle)
