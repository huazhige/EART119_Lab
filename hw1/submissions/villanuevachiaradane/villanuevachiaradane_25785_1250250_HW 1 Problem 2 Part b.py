#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Importing numpy
import numpy as np

# Function for vectorizing the area of a polygon
def area_polygon_vec(x, y):
    # In one line, we can find the area by taking the dot product
    area = 0.5*abs(np.dot(x, np.roll(y,1)) - np.dot(y, np.roll(x,1)))
    
    # Returns the area
    return area

# Test case included in the problem
x = [1, 3, 4, 3.5, 2]
y = [1, 1, 2, 5, 4]
area_polygon_vec(x, y)

