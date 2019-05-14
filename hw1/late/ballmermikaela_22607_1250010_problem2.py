#Problem 2

"""
1.) for loop
"""
import numpy                    #Allows zeros and the dot product to be used
from numpy import zeros         #Allows zeros to be used

x = zeros(6)                    #initializes a list x to be filled with 6 zeros
x[0] = 1                        #first x value
x[1] = 3                        #second x value
x[2] = 4                        #third x value
x[3] = 3.5                      #fourth x value
x[4] = 2                        #fifth x value
x[5] = 1                        #sixth x value (same as the first to connect 
                                    #the shape)

y = zeros(6)                    #initializes a list y to be filled with 6 zeros
y[0] = 1                        #first y value
y[1] = 1                        #second y value
y[2] = 2                        #third y value
y[3] = 5                        #fourth y value
y[4] = 4                        #fifth y value
y[5] = 1                        #sixth y value (same as the first to connect 
                                    #the shape)

area_polygon = 0                #area starts at 0 and then changes as new 
                                    #coordinates are plugged into the equation

for i in range(0,5):            #for loop runs the area for all values of x 
                                    #and y
    area_polygon += (0.5)*(x[i]*y[i+1]-y[i]*x[i+1])
                                #the formula for the area of the polygon
    
print('Polygon area = ' + str(area_polygon))
                                #printing the area

"""
2.) Vector Notation
"""
area_polygon_vector = 0.5*((numpy.dot(y[1:],x[:5]))-(numpy.dot(x[1:],y[:5])))
    #the formula for the area of the polygon using vector notation
    
print('Polygon area using vector notation = ' + str(area_polygon_vector))
    #printing the area