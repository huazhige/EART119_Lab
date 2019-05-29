# -*- coding: utf-8 -*-
"""
Created on Mon May 13 09:06:30 2019
Problem 1 Extra Credit Integration
Trapezoid and Midpoint Method
@author: eric_
"""
import numpy as np


#=======================================================================
#problem 1 integral of (3t^2)e^3 from t = 0 to t = 1
#=======================================================================

def function_1(t):
    return 3*t**2*np.exp(t**3)

#trapezoidal method
N = 100 #number of steps

a_t1 = np.linspace(0, 1, N+1) # time array
del_x = 1/(len(a_t1)-1) # x increment

middle_terms1 = function_1(a_t1[1:-1]) #the middle terms of trapezoid rule equation
trap_int1 = (0.5*(function_1(0)) + np.sum(middle_terms1) + 0.5*(function_1(1)))*del_x
print("Using Trapezoid Method ")
print("Integral of (3t^2)e^3 from t = 0 to t = 1 : ", trap_int1)
exact_solution1 = np.exp(1) - 1
print("Exact Solution: ", exact_solution1)
print("dx = ", del_x)
print("Error: ", exact_solution1 - trap_int1)
print("Percent Error: ", round(((exact_solution1 - trap_int1)/exact_solution1)*100, 6), "%")
print()

#
##Midpoint Method
a_t2 = np.linspace(0, 1, N+1) #time array

Midpoint = np.zeros(np.shape(a_t2))\
 
#for loop to make an array of all the midpoints
for i in range(len(a_t2) -1):
    Midpoint[i] = 0.5*(a_t2[i] + a_t2[i+1])
    
del_x2 = 1/(len(a_t2) -1 ) #x increment


#evaluating the function at the midpoints 
mid_int1 = (function_1(Midpoint).sum())*del_x2


print("Using Midpoint Method ")
print("Integral of (3t^2)e^3 from t = 0 to t = 1 : ", mid_int1)
print("Exact Solution: ", exact_solution1)
print("dx: ", del_x2)
print("Error: ", exact_solution1 - mid_int1)
print("Percent Error: ", round(((exact_solution1 - mid_int1)/exact_solution1)*100, 6), "%")








