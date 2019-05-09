# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 20:35:27 2019

@author: Brendan Chapman
"""
"""
============================================================================
Packages
============================================================================
"""
import numpy
import matplotlib.pyplot as plt
"""
============================================================================
Functions
============================================================================
"""
dec_year = []

def convert_date_time(year,month,day,hour,mins,seconds):
    dec_year = (year + (month - 1)/12) + ((day-1)/365.25) + (mins/(365.25*24*60)) + (seconds/(365.25*24*3600))
    return dec_year


def eqRate( at, k_win):
# smoothed rate from overlapping sample windows normalized by delta_t
    aS          = numpy.arange( 0, at.shape[0]-k_win, 1)
    aBin, aRate = numpy.zeros(aS.shape[0]), numpy.zeros(aS.shape[0])
    iS = 0
    for s in aS:
        i1, i2 = s, s+k_win
        aBin[iS]  = 0.5*( at[i1]+at[i2])
        aRate[iS] = k_win/( at[i2]-at[i1])
        iS += 1
    return aBin, aRate
"""
============================================================================
Text Files
============================================================================
"""
seism = numpy.loadtxt("seism_OK.txt")
injwell = numpy.loadtxt("injWell_OK.txt")



transposed_seism = seism.transpose()
transposed_injwell = injwell.transpose()



"""
============================================================================
Variables
============================================================================
"""
ID_array = transposed_seism[0]
year_array = transposed_seism[1]
month_array = transposed_seism[2]
day_array = transposed_seism[3]
hour_array = transposed_seism[4]
min_array = transposed_seism[5]
second_array  = transposed_seism[6]

"""
============================================================================
Computations
============================================================================
"""
for i in range(0,len(ID_array)-1,1):
    dec_year.append(convert_date_time(year_array[i], month_array[i], day_array[i], hour_array[i], min_array[i], second_array[i]))

for item in dec_year:
    print(item)
    
plt.hist(month_array, bins=12)

#numpy.cumsum( numpy.ones(seism))





import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap as Basemap

#------------my modules-----------------------


#===================================================================================
#                         files, variables
#===================================================================================
# This line tells computer where is the dataset, ../data means the folder which name
# is data in the previous folder, globalEqs.txt is the filename.
eqFile      = 'globalEqs.txt'
# x min and x max are the minimum value and maximum value of the latitude, respectively.
# For homework 2, you are going to specify the latitude of the region that you are
# interested in (Oklahoma).
xmin, xmax  = -180+1e-4, 180
# x min and x max are the minimum value and maximum value of the longitude.
ymin, ymax  = -90+1e-4, 90

#xmin, xmax  = -180, 0


# print the region that you are interested in.
print (xmin, xmax)
print (ymin, ymax)

#===================================================================================
#                         load data
#===================================================================================

# Read the information about time. aYr is the "array of years", np.genfromtxt is a
# function to read data from the file of the dataset (you want to import numpy for
# this function). eqFile is the path and name of the file. skip_header = 1 means that
# you want to skip the first line because that is the "header" of the file, not the data.
# usecols=(0) means that computer will read the first (python starts with 0) column and
# return this value to aYr. If you open the dataset, you will find the the year of each
# incident is ended with a dashed line, "-", so you will tell the computer that stop
# reading this line by using deliniter = "-". At last, you will tell the type of numbers
# in aYr is integer.
aYr  = np.genfromtxt( eqFile, skip_header = 1, usecols=(0), delimiter='-', dtype = int)
# Same idea with the last line, but the computer reads the second comlumn and the third
# column here, which are latitudes and longitudes of each incident.
mLoc = np.genfromtxt( eqFile, skip_header = 1, usecols=(2,1), delimiter=',', dtype = float).T
# get magnitude information and also latitude and longitude
mLoc = np.genfromtxt( eqFile, skip_header = 1, usecols=(2,1,4), delimiter=',', dtype = float).T
# sort according to year of occurrence
# This line returns the sorted index. For example, if there is a random array, (4,6,1,2),
# if I sort this array, I will get (1,2,4,6) with the smallest number to the largest.
# array.argsort will return the index of the sorted array. For example, the indices of
# each number in (4,6,1,2) are [1,2,3,4], respectively. This sentence will return [3,4,1,2]
sort_id = aYr.argsort()
# Input the sorted indices into the original time series and get the sorted time series.
aYr = aYr[sort_id]
# Input the sorted indices into the original dataset and get the sorted dataset. Transpose
# the dataset with .T
mLoc= mLoc.T[sort_id].T

#===================================================================================
#                        basemap plotting
#===================================================================================
# For each unique year in aYr.
for it in np.unique( aYr):
    sel_eq = it == aYr
    print( 'current year', it, '#no. of events: ', sel_eq.sum())
    ### create basemap object
    plt.figure( 1)
    plt.cla()
    plt.title( str( it))
    lon_0, lat_0 = .5*( xmin + xmax), .5*( ymin + ymax)
    # Input kewords and plotting parameters in this function. llcrnlon is the minimum
    # value of the longitude, urcrnrlon is the maximum value of the longitude. Similarly,
    # you are going to input information about latitude later.
    m = Basemap(projection = 'cyl',
                llcrnrlon = xmin, urcrnrlon=xmax,
                llcrnrlat = ymin, urcrnrlat=ymax,
                 resolution = 'c', lon_0 = lon_0, lat_0 = lat_0)
    m.drawcoastlines()
    # get X axis and Y axis (longitude and latitude) of the dateset from the first and the
    # second column of the dataset.
    aX_eq, aY_eq = m(  mLoc[0][sel_eq], mLoc[1][sel_eq])

    #m.plot(  aX_eq, aY_eq, 'ro', ms = 6, mew = 1.5, mfc = 'none')
    # plot the scattered points of the dataset.
    plot1 =     plt.scatter( aX_eq, aY_eq, c = mLoc[2][sel_eq], s = np.exp( mLoc[2][sel_eq]-3))
    # plot colorbar in the horizontal direction
    cbar  = plt.colorbar( plot1, orientation = 'horizontal')
    cbar.set_label( 'Magnitude')
    #--------------
    #plt.savefig(  file_out, dpi = 150)
    #
    plt.pause( .5)
    #plt.show()
    plt.clf()
    
"""
============================================================================
Part e
============================================================================
"""

"2011, and they began to decrease in 2016."
"Due to the creation of new high pressure wells"


#=================================================================================================================



"""
============================================================================
Problem 2
============================================================================
"""

"""
============================================================================
a.
============================================================================
"""

tCoord = plt.ginput( nPoints) 
#>> X = np.array( tCoord).T[0] 
#> Y = np.array( tCoord).T[1]

"""
============================================================================
b.
============================================================================
"""
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
# setup albers equal area conic basemap
# lat_1 is first standard parallel.
# lat_2 is second standard parallel.
# lon_0,lat_0 is central point.
m = Basemap(width=8000000,height=7000000,
            resolution='l',projection='aea',\
            lat_1=40.,lat_2=60,lon_0=35,lat_0=50)
m.drawcoastlines()
m.drawcountries()
m.fillcontinents(color='coral',lake_color='aqua')
# draw parallels and meridians.
m.drawparallels(np.arange(-80.,81.,20.))
m.drawmeridians(np.arange(-180.,181.,20.))
m.drawmapboundary(fill_color='aqua')
# draw tissot's indicatrix to show distortion.
ax = plt.gca()
for y in np.linspace(m.ymax/20,19*m.ymax/20,10):
    for x in np.linspace(m.xmax/20,19*m.xmax/20,12):
        lon, lat = m(x,y,inverse=True)
        poly = m.tissot(lon,lat,1.25,100,\
                        facecolor='green',zorder=10,alpha=0.5)
plt.title("Albers Equal Area Projection")
plt.show()

"""
============================================================================
c.
============================================================================
"""

A= 0.5*(((x1*y2)+(x2*y3)+(x3*y4)+(x4*y5)+(x5*y1))-((y1*x2)+(y2*x3)+(y3*x4)+(y4*x5)+(y5*x1)))
print(A)

