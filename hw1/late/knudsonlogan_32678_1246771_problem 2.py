# -*- coding: utf-8 -*-
"""
*************************************Homework 1*********************************************
    Problem 2:
    Historically, an important mathematical problem was to find the area of an irregular
    polygon, which is a key question for land usage and taxation. We will come back to
    computing the area of irregular polygons in spherical coordinates. For now, consider a
    polygon with five vertices in Cartesian coordinates: (1,1); (3,1); (4,2); (3.5, 5); (2,4).
    Write a function to compute the area of this polygon. Interestingly the area can simply
    be computed from the know vertices using the following equation:
    
    A	=	½|(x1y2 +	x2y3 +	…	xn-1yn +	xny1)	- (y1x2 +	y2x3 +	…	+	yn-1xn +	ynx1)|
   
    Your function will take two vectors (xi and yi) as input and return the area of the
    polygon A. As test cases, you can use the functions for the area of a rectangle with (0,0);
    (2,0); (2,3) and triangle with (3,1); (2,3) and (0,1) and then compute the area of the fivesided polygon. 
    Write to different functions: 1) area_polygon.py – which solves the
    above equation within a for loop and 2) area_polyon_vec.py – which solve the equation
    using vector notation
    
Annaconda 2, Python 2.7
********************************************************************************************
"""

"""
    For loop method:
        Breaking down the equation, we may match terms inside the square root so (x1y2-y1x2)+(x2y3-y2x3)+..... 
    we may write this as a sum up to N-1. So sum(x[N]y[N-1]-y[N]x[N-1]) will give us the value of the inside of the 
    root. Note, when N=0 y[N-1] = y[-1] = y[N] and the same follows for x[N-1]. To find A we will devide the sum 
    by two and we are done.
"""

#============================================
#               Importing Packages
#============================================

import numpy as np

#============================================
#               Define Varriables
#============================================

###vertecies###
ver_x_list = [1,3,4,3.5,2] #in format:  [x1,x2,x3,..,xN] 
ver_y_list = [1,1,2,5  ,4] #            [y1,y2,y3,..,xN]
###############

#============================================
#               Calculation
#============================================
A_temp = 0

def for_area (ver_x_list,ver_y_list,A_temp):
    #converts values in lists to floats
    [float(i) for i in ver_x_list] ; [float(i) for i in ver_y_list] 
    
    #looping over values in vectors
    for i in range (0,len(ver_x_list)):
        
        #performing the sum according to 
        A_temp += ver_x_list[i-1]*ver_y_list[i]-ver_y_list[i-1]*ver_x_list[i]
    
    #completes area calculation
    A = abs(A_temp)/2.
    return A

#executes the function
A = for_area(ver_x_list,ver_y_list,A_temp)
print("Area enclosed by vertecies using a for loop calculation:\n%s"%(A))

############################################################################################################
"""
    Vector method:
        We may observe the given equation and find that the first set of x1y2+... is the dot product of the 
    x vector with the y vector shifted to the left by one position. The dot product then looks like this 
                                    [x1,x2,x3](dot)[y2,y3,y1] x1y2+x2y3+x3y1,
    which is exactly what we want. The same can be done for the 2nd sum with the x vector shifted left by 
    one position. All is left is to find the absolute difference between both dot products and divide by 2.


"""

#============================================
#               Define Varriables
#============================================

###vertecies###
ver_x_list = [1,3,4,3.5,2] #in format:  [x1,x2,x3,..,xN] 
ver_y_list = [1,1,2,5  ,4] #            [y1,y2,y3,..,xN]
###############

#============================================
#               Calculation
#============================================
def vec_area (ver_x_list,ver_y_list): #defining the function to find the area of a polygon using vector calculation
    
    #creates an array out of given lists and shifts the array by 1 to the left, both arrays are saved
    ver_x_arr = np.array(ver_x_list, dtype=float) ; ver_x_roll = np.roll(ver_x_arr,-1) 
    ver_y_arr = np.array(ver_y_list, dtype=float) ; ver_y_roll = np.roll(ver_y_arr,-1)
    
    #performs calculation to give area and returns the area as A
    A = 1/2.*(np.dot(ver_x_arr,ver_y_roll)-np.dot(ver_y_arr,ver_x_roll)) 
    return A
A = vec_area (ver_x_list,ver_y_list) #executes function
print("\nArea enclosed by vertecies using vector calculation:\n%s"%(A))









