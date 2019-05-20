import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt( 'HW4_vertTraj.txt').T

z = data[1]
t = data[0]

dzdt = []

def central_dif_1(z, h):
    h = t[1]-t[0]
    for i in range(len(z)-1):  #iterating z column
        new_value = (z[i+1] - z[i])/(2*h)
        dzdt.append(new_value)
    return(dzdt)
    

    
firstderivative = central_dif_1(z, h)
#print(firstderivative[2]) #to check value

d2zdz2 = []

def central_dif_2(z,h):
    h = t[1]-t[0]
    for i in range(len(firstderivative) - 1): #iterating  first derivative
        new_value_2 = (firstderivative[i + 1] - firstderivative[i])/(h*2)
        d2zdz2.append(new_value_2)
    return(d2zdz2)
    
secondderivative = central_dif_2(firstderivative, h)
#print(secondderivative[2])  #to check value




