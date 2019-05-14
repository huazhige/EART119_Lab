#! Python 2.7
'''Problem #1 on Hw#1'''

#Test case inputs
b = 8
c = 15
height = 4

#functions
def area_of_rectangle(b,c):
    area = b*c
    return area
def area_of_triangle(height,b):
    area = 0.5*height*b
    return area

#print statements
print('Area of rectange with side lengths:',
      b,',',c,'=',area_of_rectangle(b,c))
print('Area of triangle with height',height,
      'and base length',b,'=',area_of_triangle(height,b))
