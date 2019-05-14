#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Function for area of a polygon
# The arguments include the x vector components and y vector components
def polygon_area(x, y):
    # Initializing the area
    area = 0
    
    # Setting how many vertices there are to the length of x (or y, assuming they are the same length)
    vertices = len(x)
    
    # For loop to iterate through each vertex
    for i in range(vertices):
        # This finds the index right ahead of it
        j = (i + 1) % vertices
        
        # This multiplies the x(n-1) with y(n) and sums them together
        area += x[i] * y[j]
        
        # This multiplies the x(n) with y(n-1) and subtracts them from the sum
        area -= x[j] * y[i]

    # Finding the absolute value and dividing by 2
    area = abs(area) / 2
    
    # Returns the area
    return area

