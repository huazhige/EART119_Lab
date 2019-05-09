# -*- coding: utf-8 -*-
"""
    earthquake rates
"""
# imports

#got a wierd error if I did not define the variable os
#Basemap could not find this path on its own
import os

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap as Basemap


#========================================
#                  function definitions
#========================================


def comp_rate( at, k_win):
    """
    :input 
        at = time vector of eartquakes (timestamps in Decyears)
        k_win = reference number of eartquakes
    :output
        aBin = the timestamp for each bin
        aRate = the number of eartquakes per time
    
    """
    # smoothed rate from overlapping sample windows normalized by delta_t
    aS          = np.arange( 0, len(at)-k_win, 1)
    
    aBin, aRate = np.zeros(aS.shape[0]), np.zeros(aS.shape[0])
    iS = 0
    for s in aS:
        i1, i2 = s, s+k_win
        aBin[iS]  = 0.5*( at[i1]+at[i2])
        aRate[iS] = k_win/( at[i2]-at[i1])
        iS += 1
    return aBin, aRate, aS





#=========================================
#                  files and variables
#=========================================
file_inj = 'injWell_OK.txt'
file_seism = 'seism_OK.txt'
injData = np.loadtxt(file_inj).T
seismData = np.loadtxt(file_seism).T

Mag = seismData[10,:]

TimeStamp = []
row, col = seismData.shape

def date_to_dec(YR, MO, DY, HR, MN, SC):
    DecYear = YR + (MO-1)/12 + (DY-1)/365.25 + HR/(365.25*24) 
    + MN/(365.25*24*60) + SC/(365.25*24*3600)
    return DecYear

for i in range(col):
    tempCol = seismData[:,i]
    DecYear = date_to_dec(tempCol[1], tempCol[2], tempCol[3], tempCol[4], 
                          tempCol[5], tempCol[6])
    TimeStamp.append(DecYear)

k_win = 200 #as instructed. 


#=============================================
#              compute rates
#=============================================
aBin, aRate, aS = comp_rate( TimeStamp, k_win) 
print ('aS',aS)
nbrPoints = len(aRate)


#=============================================
#                 plotting
#=============================================
plt.figure(1)

ax2 = plt.subplot( 211)
ax2.plot( aBin, aRate, 'b-')
ax2.set_xlabel( 'Time [year]'), ax2.set_ylabel( 'Rate of earthquakes ')
ax2.legend( loc = 'upper left')

ax3 = plt.subplot( 212)
ax3.plot( aBin, np.cumsum(aRate), 'g-')
# add cumulative eq number

ax3.set_xlabel( 'Time [years]')
ax3.set_ylabel( 'cumilative earthquakes')
ax3.set_xlim( ax2.get_xlim())

#==================================================
#      plotting wells and seismic activity in empty plot
#==================================================

seismX = seismData[7, :] #longitudes of earthquakes
seismY = seismData[8, :] #Latitudes of earthquakes
                   
wellX = injData[2,:] #longitudes of injection
wellY = injData[3,:] #latitudes of injections
wellTime = injData[1,:] #times of injections

#stort Well cronologically, might want earlier well though
sort_id = wellTime.argsort()
wellX = wellX[sort_id]
wellY = wellY[sort_id]
wellTime = wellTime[sort_id]


dT = 0.5
startY = 2005
endY = 2018

#Oklahomas latitudes
maxLon = -94
maxLat = 38
minLon =-103
minLat =33

for year in np.arange(startY, endY+dT, dT):
    quakes = [i for i in TimeStamp if i >= year]
    startIdx = len(TimeStamp)-len(quakes)
    quakes = [i for i in quakes if i <= year+0.5]
    endIdx = startIdx+len(quakes)

#is empty if startIdx>endIdx
    Idxs = np.arange(startIdx, endIdx, 1)
    
    
    #same procedure for finding right indexes of well data, but one time window earlier????
    wells = [i for i in wellTime if i >= 2005]
    wstartIdx = len(wellTime)-len(wells)
    wells = [i for i in wells if i <= year+0.5]
    wendIdx = wstartIdx+len(wells)
    wIdxs = np.arange(wstartIdx, wendIdx, 1)
    
    plt.figure(2)
    plt.cla()
    plt.title( str( year))
    lon_0, lat_0 = .5*( minLon + maxLon), .5*( minLat + maxLat)
    m = Basemap(projection = 'cyl',
                llcrnrlon = minLon, urcrnrlon=maxLon,
                llcrnrlat = minLat, urcrnrlat=maxLat,
                 resolution = 'c', lon_0 = lon_0, lat_0 = lat_0)
    m.drawstates()

    
    plot1 = plt.scatter(seismX[Idxs], seismY[Idxs], c = Mag[Idxs], s = 10*(Mag[Idxs]))
    m.plot(wellX[wIdxs], wellY[wIdxs], 'b +')
    cbar  = plt.colorbar( plot1, orientation = 'horizontal')
    cbar.set_label( 'Magnitude')
    
    plt.pause( .5)
    #plt.show()
    plt.clf()

#=======================================
# encapsule seismic affected areas
#=======================================
    
#plot all earthquakes that happened
image = plt.figure(3)
#need to be lcc to convert to equal distance coordinates
m2 = Basemap(projection = 'lcc',
                llcrnrlon = minLon, urcrnrlon=maxLon,
                llcrnrlat = minLat, urcrnrlat=maxLat,
                 resolution = 'c', lon_0 = lon_0, lat_0 = lat_0)

#plt.title('all Earthquakes in during the years 2005 to 2018')
quakes = [i for i in TimeStamp if i >= 2010]
startIdx = len(TimeStamp)-len(quakes)
quakes = [i for i in quakes if i <= 2018]
endIdx = startIdx+len(quakes)-1
Idxs = np.arange(startIdx, endIdx, 1)
(seismeqX, seismeqY) = m2(seismX[Idxs], seismY[Idxs])
plot2 = plt.scatter(seismeqX, seismeqY, c = Mag[Idxs], s = 10*(Mag[Idxs]))

cbar  = plt.colorbar( plot2, orientation = 'horizontal')
cbar.set_label( 'Magnitude')
m2.drawstates()

#click 10 points to encapsule area (what number of points do y'all want?)


plt.title('Click 10 points encapsuling the area, click COUNTERCLOCKWISE')
tCoord = plt.ginput(10)
X = np.array(tCoord).T[0]
Y = np.array(tCoord).T[1]
print(X)

plt.title('Selected Area')

#convert to equal distance coordinates using basemap. Its noooot converting fucking god 
eqX, eqY = m2(X,Y)


m2.plot(X,Y, 'b')
    
#define function again here
def area_polygon_vec(l_x, l_y):
    """
    - computes the area of polygon with vertices defined by 
    position vectors l_x and l_y
    
    :input
    l_x = the x-coordinates of the vertices
    l_y = the y-coordinates of the vertices in the same order as l_x
    
    :output
    A = the area of the polygon
    """
    x_N = len(l_x)
    y_N = len(l_y)
    
    if x_N != y_N:
        return -1
    else:
        l_y_shift = np.concatenate((l_y[1:y_N], l_y[0]),axis=None)
        x_sum = np.dot(l_x,l_y_shift, out=None) #elementwise multiplicaction
        
        l_x_shift = np.concatenate((l_x[1:x_N],l_x[0]),axis=None)
        y_sum = np.dot(l_y,l_x_shift, out=None)
        
        A = 0.5*abs(x_sum-y_sum)
        
        return A
    
Area = area_polygon_vec(X/1000, Y/1000)#convert to km
oakArea= 181000
print(Area)


ratio = 100*Area/oakArea
print(ratio)

titleName = 'the affected area is ' + str(round(Area,2)) + ' km^2, which is ' + str(round(ratio)) + '% of the total area of Oklahoma'
plt.title(titleName)

