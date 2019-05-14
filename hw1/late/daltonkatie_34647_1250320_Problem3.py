# -*- coding: utf-8 -*-
"""

        one circle and one rectangle
        circle radius = 12.6 #mm
        rectangle area = a x b
            a = 1.5 #mm
            b = ?
        find highest values of b while rect_area < cir_area

"""
import numpy as np

#find area of the circle
r = 12.6
cir_area = np.pi*(r**2)

#start with the minimum value of b possible to start the rectangle area
a = 1.5
b = 0
rect_area = a * b 

#add one to b everytime rectangle area is less than circle area
#add one to keep as int
while rect_area < cir_area:
    b += 1
    rect_area = a * b

#while loop will add one more to make rect_area greater than cir_area
#so subtract one from b to stll be less than circle area
b = b-1
print(b)