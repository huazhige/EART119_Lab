# -*- coding: utf-8 -*-
"""
Calculates area of rectangle and triangle 
"""

c = float(raw_input('Rectangle width:  '))
b = float(raw_input('Rectangle (and triangle) height:  '))
h_b = float(raw_input('Base of triangle width:  '))

A_rec = b*c
A_tri = 0.5*b*h_b

print('\nRectangle area: ' + str(A_rec))
print('Triangle area: ' + str(A_tri))