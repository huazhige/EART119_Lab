import numpy as np
import matplotlib.pyplot as plt

#===================================================================================
#                          importing and loading data
#===================================================================================
data = np.genfromtxt('midterm_dydx.txt').T

t =data[0]
z =data[1]


#===================================================================================
#                          central difference method
#===================================================================================
dzdt = [] #assigning an empty set to itterate later

def cen_diff(z, h): #itteration
    h = t[1]-t[0]
    for i in range(len(z)-1):
        new_value = (z[i+1]-z[i])/(2*h)
        dzdt.append(new_value)
    return(dzdt)

firstderivative = cen_diff(z, h)
#print(firstderivative)

d2zdz2 = []

def central_dif_2(z,h):
    h = t[1]-t[0]
    for i in range(len(firstderivative) - 1): 
        new_value_2 = (firstderivative[i + 1] - firstderivative[i])/(h*2)
        d2zdz2.append(new_value_2)
    return(d2zdz2)
    
secondderivative = central_dif_2(firstderivative, h)
#print(secondderivative[2])



#===================================================================================
#                          plotting functions
#===================================================================================
plt.plot(t,z)
plt.subplot(firstderivative, secondderivative)
plt.title('t vs z and Its derivatives')
plt.xlabel('z values')
plt.ylabel('t values')
plt.show()
#plt.savefig
