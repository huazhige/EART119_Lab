# -*- coding: utf-8 -*-
"""
Calculates the area of an irregular polygon using a for loop.
"""

x_input = raw_input('Enter 5 x-coords separated by a space: ')
x = x_input.split()
y_input = raw_input('Enter 5 y-coords separated by a space: ')
y = y_input.split()

def Area_poly(x_coords,y_coords):
    A = 0
    
    for i in range(len(x)): 
        if i < (len(x) - 1):        
            A += float(x[i])*float(y[i+1])
            A -= float(y[i])*float(x[i+1])        
        if i == (len(x) - 1):        
            A += float(x[i])*float(y[0])
            A -= float(y[i])*float(x[0])

            A = 0.5*abs(A)
            return A

Area = Area_poly(x_input,y_input)

print('\nThe area is: ' + str(Area))