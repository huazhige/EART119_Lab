# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 18:22:01 2019
Geographical Seimisicity after 2013
@author: eric_
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap as Basemap

file_in = "seism_OK.txt"
year_vector = np.array(np.genfromtxt(file_in, skip_header = 1, usecols = (1))).T
boolean_array = year_vector > 2012

longitude = np.array(np.genfromtxt(file_in, skip_header = 1, usecols =(7),\
                                   dtype = float))
latitude = np.array(np.genfromtxt(file_in, skip_header = 1, usecols = (8), dtype =\
                                  float))
longitude = longitude[boolean_array]
latitude = latitude[boolean_array]


#print(year_vector)
#parameter for longitude and latitude
xmin, xmax  = -101, -94
ymin, ymax  = 33.5, 37.1

#tCoord = plt.ginput( nPoints)
#x = np.array( tCoord).T[0]
#y = np.array( tCoord).T[1]

#area of irregular polygon
def area(x_vector, y_vector):
    x1 = np.roll(x_vector, -1) #roll command moves each index by -1 
    y1 = np.roll(y_vector, -1)
    #print("x-vector = ", x_vector)
    #print("y-vector = ", y_vector)
    #print("x1 = : ", x1)
    #print("y1 = : ", y1)
    total_area = (0.5)*(np.dot(x_vector, y1) - np.dot(y_vector, x1)) #area of irregular polygon
    return(total_area)
    
#==========================================================================
#               scatter plot of seismicity
#==========================================================================

m = Basemap(projection = "aea", width = 8e6, height = 7e6, \
            lat_0 = 35, lon_0 = -97.5, llcrnrlon = xmin, llcrnrlat = ymin,\
            urcrnrlon= xmax, urcrnrlat = ymax, resolution = 'c')

ax1, ax2 = m(longitude, latitude)
"""m = Basemap(projection = "cyl", llcrnrlon = -179, llcrnrlat = -89, \
            urcrnrlon= 179, urcrnrlat = 89, resolution = 'c')"""
m.drawcoastlines()
m.drawcountries()
m.drawstates()
plot1 = plt.scatter(ax1, ax2)
#find approximate area of seismicity
N = 30 #number of inputs
tCoor = plt.ginput(N)
x = (1/1000)*np.array(tCoor).T[0]
y = (1/1000)*np.array(tCoor).T[1]
plt.show()

print("x-vector: ", x)
print("y-vector: ", y)
print("Area of region : ", area(x, y), "kilometers squared")

#the area of the region is about 111,111 km squared
#over half the size of Oklohoma





