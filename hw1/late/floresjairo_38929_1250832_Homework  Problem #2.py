
"""
Jairo Flores 
Problem #2
"""
#////////////////Problem 2///////////////////////////////
"A program that finds the area of polygon using vectors and loops"
 
#Import numpy Libary.
import numpy as np

#create vectors
x = np.array([1,3,4,3.5,2])
y = np.array([1,1,2,5,4])

#Create Function///////////////////////
def area_polygon (x,y):
    i = 0
    area = 0
    while i < 4:
        area += .5*(x[i]*y[i+1])-(y[i]*x[i+1])
        i += 1
    return abs(area)
#/////////////////////////////////////

print("The area of the polygon is ")
print(area_polygon(x,y))

