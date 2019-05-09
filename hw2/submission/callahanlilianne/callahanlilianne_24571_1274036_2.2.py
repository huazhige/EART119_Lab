# -*- coding: utf-8 -*-
"""
Homework #2, Problem 2

Lili Callahan

This problem computes the area of OK affected by seismicity from 2010-2017 
and the fraction of OK that area takes up.

"""
#   Problem 2
#   a) 

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

##############################################################################
#   Files and parameters
##############################################################################

file1 = "injWell_OK.txt"
file2 = "seism_OK.txt"

##############################################################################
#   Load data
##############################################################################

data1 = np.loadtxt(file1, skiprows = 1)
data2 = np.loadtxt(file2, skiprows = 1).T

##############################################################################
#   Convert time columns to decimal years
##############################################################################

YR = data2[1 ,:]
MO = data2[2 ,:]
DY = data2[3 ,:]
HR = data2[4 ,:]
MN = data2[5 ,:]
SC = data2[6 ,:]

DecYear = YR + (MO-1)/12 + (DY-1)/365.25 + HR/(365.25*24) + MN/(365.25*24*60) + SC/(365*24*3600)

dPar  =  {   'nClicks' : 1,
             'tmin'    : 2010,
             'areaOK'  : 181*1e3,
             'dt_map'  : 6./12,
             # Basemap parameters
             'xmin' : -101, 'xmax' : -94,
             'ymin' : 33.5, 'ymax' : 37.1,
             'projection' : 'aea',
           }

##############################################################################
#   Select boundaries of seismicity
##############################################################################

plt.figure(1)
ax1 = plt.subplot(111)

aT = DecYear
data2 = np.array([aT, data2[7], data2[8], data2[-1]])
sel = np.logical_and(DecYear >= 2010, DecYear <= 2017)
#data2 = data2.T[sel].T
data1 = np.loadtxt(file1).T

print("Please click %i times"%( dPar['nClicks']))
tCoord = plt.ginput( dPar['nClicks'])
print("clicked", tCoord)
plt.show()

at_bin = np.arange(dPar['tmin'], 2018, dPar['dt_map'])
for i in range( at_bin.shape[0]-1):
    t1, t2 = at_bin[i], at_bin[i+1]
    sel_eq = np.logical_and( data2[0] >= t1, data2[0] < t2)
    sel_wells = np.logical_and( data1[1] <= t1, data1[1] < t1)
    print(t1, t2, 'No. earthquakes: ', sel_eq.sum(), 'No. of wells: ', sel_wells.sum())

    plt.figure(1)
    plt.cla()
    ax2 = plt.subplot(111)
    lon_0, lat_0 = .5*( dPar['xmin']+dPar['xmax']), .5*( dPar['ymin']+dPar['ymax'])
    m = Basemap(llcrnrlon = dPar['xmin'], urcrnrlon=dPar['xmax'],
                llcrnrlat = dPar['ymin'], urcrnrlat=dPar['ymax'],
                lon_0 = lon_0, lat_0 = lat_0,
                resolution = 'l',
                projection = dPar['projection'])
    
    m.drawcoastlines()
    aX_we, aY_we = m(data1[2][sel_wells], data1[3][sel_wells])
    m.plot(aX_we, aY_we, 'ro', ms = 2)
    aX_eq, aY_eq = m(data2[1][sel_eq], data2[2][sel_eq])
    m.plot(aX_eq, aY_eq, 'bo', ms = 2)
    m.drawparallels(np.arange(33, 38, 1), fmt = '%i', labels = [1, 0 , 0 , 0])
    m.drawmeridians(np.arange(-100, -92, 2), fmt = '%i', labels = [0, 0 , 0 , 1])
    print("Please click %i times"%( dPar['nClicks']))
    tCoord = plt.ginput( dPar['nClicks'])
    print("clicked", tCoord)
    plt.show()
    aLon = np.array(tCoord).T[0]
    aLat = np.array(tCoord).T[1]

#   b)
   
##############################################################################
#   Project into an equal-distance coordinate system
##############################################################################

lon_0, lat_0 = .5*( dPar['xmin']+dPar['xmax']), .5*( dPar['ymin']+dPar['ymax'])
m = Basemap(llcrnrlon = dPar['xmin'], urcrnrlon=dPar['xmax'],
            llcrnrlat = dPar['ymin'], urcrnrlat=dPar['ymax'],
            projection=dPar['projection'], lon_0 = lon_0, lat_0 = lat_0)

#   c)

##############################################################################
#   Compute affected area
##############################################################################

def area_poly(aX, aY):
    sumVert1 = np.dot(aX[0:-1], aY[1::])+aX[-1]*aY[0]
    sumVert2 = np.dot(aY[0:-1], aX[1::])+aY[-1]*aX[0]
    return 0.5*abs(sumVert1 - sumVert2)

aX, aY = (aX_we/1000, aY_we/1000) 
a_seis = area_poly(aX, aY)
print('Total area affected by seismicity: ', a_seis)
print('Fraction of area of OK: ', a_seis/(dPar['areaOK']))

"""
I am pretty sure I was supposed to say
aX, aY = (aX_eq/1000, aY_eq/1000)
on line 126, but doing so did not get me close to 1/3.

"""





