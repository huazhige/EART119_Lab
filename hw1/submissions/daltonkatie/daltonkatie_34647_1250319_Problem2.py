# -*- coding: utf-8 -*-
"""
        find the area of an irregular polygon
        use:
        A =	½|(x1y2 + x2y3 + … xn-1yn +	xny1) - (y1x2 +	y2x3 + … + yn-1xn +	ynx1)|
"""
#------------------------------------------------------------------
#       Parameters
#------------------------------------------------------------------
import numpy as np
x = []
y = []
first_sum = 0
second_sum = 0

#need input of how many time to go through the for loop
n = int(raw_input("How many verticies?"))


#-----------------------------------------------------------------
#       For loop to create list
#-----------------------------------------------------------------


#for loop to get the coordinates
for i in range(n):
    x_input = float(raw_input("Enter the x-coordinate of one vertex."))
    y_input = float(raw_input("Enter the y-coordinate for the same vertex."))
    #add the user input into a list
    x.append(x_input)
    y.append(y_input)
    
#----------------------------------------------------------------
#       For loop to use the given equation
#----------------------------------------------------------------

for d in range(n-1):
    half_1 = (x[d]*y[d+1]) #used for all pieces except for the last xn*y1 in the first half
    first_sum += half_1
    half_2 = (y[d]*x[d+1]) #used for all pieces expect for the last yn*x1 in second half
    second_sum += half_2

#now to include xn*y0 and yn*x0 respectively
lastbit1 = x[len(x)-1]*y[0]
lastbit2 = y[len(y)-1]*x[0]

#connect the parts of the halves
total_half1 = first_sum + lastbit1
total_half2 = second_sum + lastbit2

#use the equation
A = (0.5)*abs(total_half1 - total_half2)
print(A)

#-------------------------------------------------------------------
#       Using vector notation
#-------------------------------------------------------------------

#use the roll function to offset the lists correctly
#dot the offset list and the other list together to get the whole sum of some side
y_new = np.roll(y,4)
v_sum1 = np.dot(x,y_new)
x_new = np.roll(x,4)
v_sum2 = np.dot(x_new,y)

A = (0.5)*abs(v_sum1 - v_sum2) #same equation as before
print(A)