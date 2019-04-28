# -*- coding: utf-8 -*-
"""
Collin O'Connor
Homework 1
"""


import numpy as np

#==============================================================================
#Question 1
#==============================================================================
def area_rectangle(b,c):
    A=b*c
    return("Area of rectangle is %.2f" %(A))
def area_triangle(h_b,b):
    A_triangle=0.5*h_b*b
    return("Area of triangle is %.2f" %(A_triangle))

#==============================================================================
#Question 2
#==============================================================================
#==============================================================================
#part a
#==============================================================================
def area_polygon(x,y):
    n = len(x)
    area = x[n-1]*y[0] - y[n-1]*x[0]  
    for i in range(0,n-1,1):
        area += x[i]*y[i+1] - y[i]*x[i+1]
    return 0.5*abs(area)
x=[1,3,4,3.5,2]
y=[1,1,2,5,4]
print("Area of polygon is %.2f" %area_polygon(x,y))

#==============================================================================
#part b
#==============================================================================
def area_polygon_vector(a,b):
    return 0.5*np.abs(np.dot(a,np.roll(b,1))-np.dot(b,np.roll(a,1)))
a=[1,3,4,3.5,2]
b=[1,1,2,5,4]
print("Area of polygon using vector notation is %.2f"  %area_polygon_vector(a,b))

#==============================================================================
#Question 3
#==============================================================================
r=12.6
e=1.5
circle_area = np.pi*r**2
f=0 #smallest possible value and from here we'll work our way up
while e*f < circle_area: #Using e*f becuase this is what will give us area of rectangle
    f+=1
f=f-1    #the only way for the while loop to exit is when the rectangle area is bigger than the circle's. So that means that the b value produced after the while loop exits itelf is one integer value larger than it needs to be if the rectangle area is going to be smaller than the cirlce's
print ("The value of b is %d" %f)

#==============================================================================
#Bonus Question
#==============================================================================
#==============================================================================
#Part a
#==============================================================================
def radio_decay(initial,t,half_t): #arguments must be put in as floats or else function will return false/improper values.
    if initial==0:                 #initial would be zero if we don't have any initial amount given for us to input. Therefore, this function will determine the fraction of however much of a substance remains
        return(np.exp(-t/half_t))
    else:
        return(initial*np.exp(-t/half_t))

#==============================================================================
#part b
#==============================================================================
pm=np.array([+40,-40]) #pm stands for plus/minus
c14_half=5730+pm
def c14_radio_decay(t,half_t): #arguments must be put in as floats or else function will return false improper values.
    return(100*np.exp(-t/half_t))

print('percent of c14 remaining after 10k years')
print(c14_radio_decay(10e3, c14_half))#The array produced from this gives the maximum percent of the initial given value on the first spot and the minimum on the second spot

print"percent c14 remaining after 100k years"
print(c14_radio_decay(100e3, c14_half))#The array produced from this gives the maximum percent of the initial given value on the first spot and the minimum on the second spot


print"percent c14 remaining after 1M years"
print(c14_radio_decay(1e6, c14_half))#The array produced from this gives the maximum percent of the initial given value on the first spot and the minimum on the second spot


#==============================================================================
#part c
#==============================================================================
user_t=float(input())
user_t_half=float(input())
def input_radio_decay(t,half_t): 
    return(np.exp(-t/half_t))
print(input_radio_decay(user_t, user_t_half))




