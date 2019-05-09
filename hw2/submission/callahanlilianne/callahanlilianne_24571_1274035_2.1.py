#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Homework #2, Problem 1

Lili Callahan

This problem graphes the number of earthquakes and cumulative number with 
repect to time. It also graphs the location of earthquakes and active wells 
in OK from 2005-2017.

"""

#   Problem 1
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

#   b)

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
 
#   c)

dPar  =  {   'showRate'  : True,
             'dt_map'    : 6./12,
             'k'         : 200,
             'tmin'      : 2005, 
             #  Basemap parameters
             'xmin' : -101, 'xmax' : -94,
             'ymin' :   33.5, 'ymax' :  37.1,
             'projection' : 'aea',
           }

##############################################################################
#   Determine earthquake rate and cumulative number
##############################################################################

if dPar['showRate'] == True:
    plt.figure(1)
    ax = plt.subplot(211)

#   Earthquake rate   
k = 200
at = DecYear
def comp_rate(at, k):
    aS = np.arange(0, at.shape[0]-k)
    aBin, aRate = np.zeros(aS.shape[0]), np.zeros(aS.shape[0])
    iS = 0
    for s in aS:
        i1, i2 = s, s+k
        aBin[iS] = 0.5*(at[i1]+at[i2])
        aRate[iS] = k/(at[i2]-at[i1])
        iS += 1
    return aBin, aRate

aBin = comp_rate(at, k)[0]
aRate = comp_rate (at, k)[1]

#   Cumulative number
cum_num = np.cumsum(np.ones(7000))

##############################################################################
#   Plotting 
##############################################################################
    
#   Plotting rates
plt.subplot(211)
plt.plot(aBin, aRate)
plt.xlabel("Time (mo)")
plt.ylabel("Earthquake rate (ev/mo)")
plt.show()

#   Plotting cumulative number

plt.subplot(212)
plt.plot(aBin, cum_num)
plt.xlabel("Time (dec. years)")
plt.ylabel("Cumulative number")
#plt.set_xlim(ax.get_xlim())
plt.show()

#   d)

##############################################################################
#   Active wells plot
##############################################################################

data2 = np.array([at, data2[7], data2[8], data2[-1]])
data1 = np.loadtxt(file1).T

at_bin = np.arange(dPar['tmin'], 2018, dPar['dt_map'])
for i in range( at_bin.shape[0]-1):
    t1, t2 = at_bin[i], at_bin[i+1]
    
    sel_eq = np.logical_and( data2[0] >= t1, data2[0] < t2)
    sel_wells = np.logical_and( data1[1] <= t1, data1[1] <= t1)
    print(t1, t2, 'No. earthquakes', sel_eq.sum(), 'No. of wells', sel_wells.sum())

    plt.figure(2)
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
    plt.pause(0.5)
    plt.clf()

#   e)
    
"""
The year that seismicity rates exceeded historical value was 2010. They started 
to decrease in 2017. I suspect that this is because people stopped injecting to 
create man-made earthquakes.

"""

