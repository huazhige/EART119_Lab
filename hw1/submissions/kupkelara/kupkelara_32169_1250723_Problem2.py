#!Python 2.7
'''
Problem #2 on Hw#1
Compute the area of a polygon with loops and vector notation
'''
#Test cases
#points=((3,1),(2,3),(0,1))
#points=((0,0),(2,0), (2,3))
points= ((1,1), (3,1), (4,2), (3.5, 5), (2,4))

#import
import numpy as np

#Functions

def while_area_polygon(points): #area computed by while loop
    summation = 0
    difference = 0
    maximum = len(points) - 1
    i = 0
    while i <= maximum:
        difference = (np.array(points)[i, 0]*np.array(points)[i-1, 1]) - (np.array(points)[i-1, 0]*np.array(points)[i,1])
        summation = summation + difference
        i = i + 1
    area = .5*abs(summation)
    return area
print('Using while we get:',while_area_polygon(points))

def for_area_polygon(points): #area computed by for loop
    """Given x,y, coordinates, computes the area using a for loop"""
    summation = 0
    difference = 0
    maximum = len(points)
    for i in range(maximum):
        difference = (np.array(points)[i, 0]*np.array(points)[i-1, 1]) - (np.array(points)[i-1, 0]*np.array(points)[i, 1])
        summation = summation+difference
        i = i + 1
    area = .5*abs(summation)
    return area
print('Using for we get:',for_area_polygon(points))

def vec_area_polygon(points): #computed without loops
    """Given x,y, coordinates, computes the area using arrays"""

    array = np.array(points)
    xvec = array[:, 0]
    yvec = array[:, 1]
    offsettxvec = np.roll(xvec, -1) #shifts/rotates the area values by -1
    offsettyvec = np.roll(yvec, -1)
    part1 = xvec*offsettyvec
    part2 = yvec*offsettxvec
    summation = (sum(part1-part2))
    area = .5*abs(summation)
    print(part1)
    print(part2)
    print summation
    return area
print('Using vector notation we get:', vec_area_polygon(points))
