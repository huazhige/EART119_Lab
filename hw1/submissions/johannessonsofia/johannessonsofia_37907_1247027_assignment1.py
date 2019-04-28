# -*- coding: utf-8 -*-
#variables

b_rectangle = False
f_b_rc = 2
f_c = 6

b_triangle = True
f_h = 4
f_b_tr = 5

"""
    - computes the area of a triangle if the first parameter
    true and area of rectangle first parameter is false
    :input
    isTriangle = true if triangle and false if rectangle
    f_b = base of the triangle or rectange
    f_h = height of the triangle or rectangle

    :output
    f_A = area of triangle
"""
def assigment1(isTriangle, f_b, f_h):
    if(isTriangle):
        A = 0.5*f_b*f_h;
    else:
            A = f_b*f_h
            
    return A

print('triangle area', assigment1(b_triangle, f_b_tr, f_h))
print('rectangle area', assigment1(b_rectangle, f_b_rc, f_c))