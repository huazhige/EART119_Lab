#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Importing numpy
import numpy as np

# Parameters for the circle's area
r = 12.6
A_circ = np.pi*r**2

# Parameters for the rectangle's area
a = 1.5
b = 0
A_rect = a*b

# While loop: while the circle's area is larger than the rectangle's
while A_circ > A_rect:
    # Acts as a counter and adds 1 to b every time until the area of the rectangle is larger
    b += 1
    
    # Finds the area of the rectangle
    A_rect = a*b
    
# If loop added so that if the last iteration of the rectangle is larger, this subtracts 1 from b
# So that the rectangle's area is just less than the circle's
if A_rect > A_circ:
    b -= 1

# Finds the final area of the rectangle
A_rect = a*b

# Prints what the final areas are
print("The area of the circle is %.2f mm." % A_circ)
print("The area of the rectangle is %.2f mm with b = %.2f mm." % (A_rect, b))

