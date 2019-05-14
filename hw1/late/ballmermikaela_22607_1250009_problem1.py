#Problem 1

b  = input('base: ')                       #base
c  = input('side: ')                       #side of rectangle
h = input('height: ')                      #height of triangle

def A_rectangle(b,c):                      #defining the function A_rectangle
    A = (b)*(c)                            #Area or rectangle
    print('Area of rectangle = '+ str(A))  #printing the area

area_rectangle = A_rectangle(b,c)          #calling the function

def A_triangle(b,h):                       #defining the function A_triangle
    A  = 0.5*(h)*(b)                       #Area of triangle
    print('Area of triangle = '+ str(A))   #printing the area
    
area_triangle = A_triangle(b,h)            #calling the function