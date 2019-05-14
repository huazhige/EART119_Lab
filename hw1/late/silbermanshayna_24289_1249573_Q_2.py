# -*- coding: utf-8 -*-

# points = ( 1, 1), ( 3, 1), ( 4, 2), ( 3.5, 5), ( 2, 4)

def area_poly ( x, y):
    # x = x vector with n points
    # y = y vector with n points
    # Sum = first sum up to x_n-1*y_n + x_n*y_1
    Sum = 0
    for i in range (0, len(x) - 1):
        Sum += x[i]*y[i + 1]
        
    Sum += x[len(x) - 1]*y[0]
    
    # Sum2 = sum up to y_n-1*x_n + y_n*x_1
    Sum2 = 0   
    for i in range (0, len(x) - 1):
        Sum2 += y[i]*x[i + 1]
        
    Sum2 += y[len(x) - 1]*x[0]
    
    FinalSum = .5*(Sum - Sum2)
    return FinalSum


x = [0,2,2]
y = [0,0,3]
print( area_poly( x, y))
        
#x = [3,2,0]
#y = [1,3,1]
#print( area_poly( x, y))
        
        
        
        
        
        
