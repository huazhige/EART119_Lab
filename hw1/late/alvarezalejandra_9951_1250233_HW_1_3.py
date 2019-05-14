# -*- coding: utf-8 -*-

import numpy as np
 #find area of circle
a_circle = np.pi * 12.6**2

#set initial parameters for rectangle
a = 1.5
b = 1

#increase length of b by 1 UNTIL area of rectangle exceeds a_circle
while a*b < a_circle:
    b = b+1

#print correct value of b
print(b)

