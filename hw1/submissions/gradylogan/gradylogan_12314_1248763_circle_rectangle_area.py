# -*- coding: utf-8 -*-
import math
#========================
r = 12.6
a_circ = (math.pi)*r**2
print a_circ
#========================

a      = 1.5
b      = 0
a_rect = a*b

while a_rect < a_circ:
    b = b + 1
    a_rect = a*b
    print b

 