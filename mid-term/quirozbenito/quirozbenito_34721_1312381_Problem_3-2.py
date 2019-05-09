#-*- coding: utf-8 -*-
"""
Benny Quiroz
1680808
Problem 3
"""
import numpy as np
import matplotlib.pyplot as plt
import os 

#Loads in our data
path = 'C:\\Users\\benit\\Python Scripts\\119 Midterm'
os.chdir(path)
file_in = 'midterm_dydx.txt'
func = np.loadtxt(file_in, comments = '#').T

#Creates an array that will be 2 shorter than function that way we can place the
#initial value of the 2nd D at time = 0 instead of at t1. It also emilinates a zero at the
#End of the array which makes the graph messy. 
firstd = np.array([np.zeros(len(func[0]) - 2), np.zeros(len(func[0]) - 2)])
#This is just the central difference method but instead of picking a delta t, the
#time data does that for us. 
for i in range(1, len(func[1]) - 1):
    firstd[0][i-1] = func[0][i-1]
    #Slightly different from formula as this spans the whole bin and is not plus
    #and minus the same value from the middle of the bin. 
    deltat = func[0][i+1] - func[0][i-1]
    firstd[1][i - 1] = (func[1][i+1] - func[1][i-1])/(deltat)
    
#Same as 1st D. 
secondd = np.array([np.zeros(len(firstd[0]) - 2), np.zeros(len(firstd[0]) - 2)])
for i in range(1, len(firstd[1]) - 1):
    secondd[0][i-1] = firstd[0][i-1]
    deltat = firstd[0][i+1] - firstd[0][i-1]
    secondd[1][i - 1] = (firstd[1][i+1] - firstd[1][i-1])/(deltat)
    

#Just gonna go ahead and graph function and its derivatives on 3 differnt subplots. 
plt.cla()
plt.figure(1)
plt.tight_layout()

plt.subplot(311)
plt.plot(func[0], func[1], 'b-')
plt.plot(func[0], func[0]*0, 'k-', label = 'y = 0')
plt.xlabel('x')
plt.ylabel('z')
plt.legend()
plt.title('Function')

plt.subplot(312)
plt.plot(firstd[0], firstd[1], 'g-')
plt.plot(func[0], func[0]*0, 'k-')
plt.xlabel('x')
plt.ylabel('y')
plt.title('First Derivative')

plt.subplot(313)
plt.plot(secondd[0], secondd[1], 'r-', lw = 1)
plt.plot(func[0], func[0]*0, 'k-')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Second Derivative')

plt.show()