# -*- coding: utf-8 -*-

import numpy as np
import math

r = 12.6 #mm
a = 1.5 #mm
b = 0

Area_circ = 2*math.pi*r


while Area_rect < Area_circ:
    Area_rect = a*b
    b += 1

print Area_rect


