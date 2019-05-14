# -*- coding: utf-8 -*-



# A_r = b*c
# A_t = (.5)*h*b

# b = length of rect and base of triangle (5)
# c = width of rectangle (2)
# h = height of triangle (4)

def area_of_rect ( b, c):
    A_r = b*c
    return A_r
def area_of_tri ( h, b):
    A_t = (.5)*h*b
    return A_t

print( area_of_rect( 5, 2))
print( area_of_tri( 4, 5))