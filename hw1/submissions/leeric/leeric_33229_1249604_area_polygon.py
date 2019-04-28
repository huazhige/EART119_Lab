# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 19:00:45 2019

@author: eric_
"""
x = [] #x-coordinate as a list
y = [] #y-coordinate as a list
sum1 = 0
sum2 = 0
n = int(input("how many vertices? ")) #number of vertices
for i in range(n):
    print("Give Coordinates as a float for vertex ", i+1)
    x_coor = float(input("x-coordinate for vertex: "))
    y_coor = float(input("y-coordinate for vertex: "))
    x.append(x_coor) #adding elements into list
    y.append(y_coor)
for l in range(n-1):
    first_sum = (x[l]*y[l+1]) #Elements in first series in the equation
    sum1 += first_sum
    second_sum = (y[l]*x[l+1]) #Second Series in the equation
    sum2 += second_sum
first1 = x[len(x)-1]*y[0] # xn*y1
second1 = y[len(y)-1]*x[0] #yn*x1
mom = sum1 + first1 #summation of first series
dad = sum2 + second1 #summation of second series
A = (0.5)*(mom - dad) #Area of irregular polygon
print("Area = ", A)
