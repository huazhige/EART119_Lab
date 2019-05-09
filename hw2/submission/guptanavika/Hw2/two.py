# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 22:44:24 2019

@author: ngupta12
"""

#!/bin/python2.7
"""

--> 1) load OK seismicity and well data
--> 2) plot eqs and wells using matplotlib
--> 3) select polygon that encompasses seism., project to equal area
       and compute area of polygon



"""
#from __future__ import division
import os
import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.basemap import Basemap

#------------my modules-----------------------
#import seis_utils


#===================================================================================
#                         rate computation
#===================================================================================
def eqRate( at, k_win):
    # smoothed rate from overlapping sample windows normalized by delta_t
    aS          = np.arange( 0, at.shape[0]-k_win, 1)
    aBin, aRate = np.zeros(aS.shape[0]), np.zeros(aS.shape[0])
    iS = 0
    for s in aS:
        i1, i2 = s, s+k_win
        aBin[iS]  = 0.5*( at[i1]+at[i2])
        aRate[iS] = k_win/( at[i2]-at[i1])
        iS += 1
    return aBin, aRate

#===================================================================================
#                         time and distance
#===================================================================================
def haversine( lon1, lat1, lon2, lat2, **kwargs):
    """
    haversine formula implementation
    https://en.wikipedia.org/wiki/Great-circle_distance
    great circle distance between two points
    :input   lon1, lat1
             lon2, lat2

    		  gR - Earth radius (global variable)
    :output  distance - great circle distance in meter
    """
    gR = 6378.137 # ~6370
    # convert to radians
    lon1 = lon1 * np.pi / 180
    lon2 = lon2 * np.pi / 180
    lat1 = lat1 * np.pi / 180
    lat2 = lat2 * np.pi / 180
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))
    distance = gR * c
    return distance

def dateTime2decYr( YR, MO, DY, HR, MN, SC):
    """
    - convert date time to decimal year
    :param YR: - int or arrays
    :param MO:
    :param DY:
    :param HR:
    :param MN:
    :param SC:
    :return:
    """
    nDays = 365.25
    return YR + (MO-1)/12 + (DY-1)/nDays  + HR/(nDays*24) + MN/(nDays*24*60) + SC/(nDays*24*3600)

def area_poly( aX, aY):
    """
    use:

    A = 0.1*abs( (x1*y2 + x2*y3 + xn-1*yn + xn*y1) - (y1*x2 + y2*x3 + ... + yn-1*xn + yn*x1))
    :param aX: - x-coordinates of all vertices
    :param aY: - y-coordinates of all vertices
    :return: A - area of polygon
    """
    #sumVert1 = (aX[0:-1]*aY[1::]).sum()+aX[-1]*aY[0]
    # or:
    sumVert1  = np.dot( aX[0:-1], aY[1::])+aX[-1]*aY[0]
    #sumVert2 = (aY[0:-1]*aX[1::]).sum()+aY[-1]*aX[0]
    # or:
    sumVert2  = np.dot(aY[0:-1], aX[1::])+aY[-1]*aX[0]
    #sum = (aX[0:-1]*aY[1::] - aY[0:-1]*aX[1::]).sum() + (aX[-1]*aY[0]-aY[-1]*aX[0])
    return 0.5*abs( sumVert1 - sumVert2)
#--------------------------0---------------------------------------------
#                     params, dirs, files
#------------------------------------------------------------------------
#data_dir   = ???
file_eq    = 'seism_OK.txt'
file_well  = 'injWell_OK.txt'

dPar  =  {   'nClicks' : 10,
             'tmin'    : 2010,
             'areaOK'  : 181*1e3,#in km
             # -----basemap params----------------------
             'xmin' : -101, 'xmax' : -94,
             'ymin' :   33.5, 'ymax' :  37.1,
             'projection' : 'aea',# or 'cea' 'aea' for equal area projections
           }

#--------------------------1---------------------------------------------
#                        load data
#------------------------------------------------------------------------
#  os.chdir( data_dir)
# load seismicity and well data using loadtxt
mSeis  = np.loadtxt( file_eq).T
#:TODO data-time to decimal years


yr=mSeis[1]
mon=mSeis[2]
dy=mSeis[3]
hr=mSeis[4]
mn=mSeis[5]
sec=mSeis[6]
lon=mSeis[7]
lat=mSeis[8]

#print yr[1]

aTime = np.empty(len(yr))

for i in range(len(yr)-1):
	aTime[i]=dateTime2decYr( yr[i], mon[i], dy[i], hr[i], mn[i], sec[i])




mSeis  = np.array( [aTime, mSeis[7], mSeis[8], mSeis[-1]])
#TODO: select most recent seismic events
sel   = np.logical_and( mSeis[0]  >= 2009, mSeis[0]   < 2017.5)
mSeis  = mSeis.T[sel].T
mWells = np.loadtxt( file_well).T

#--------------------------2---------------------------------------------
#                       map view, select boundaries of seismicity
#------------------------------------------------------------------------
plt.figure(1)
ax1 = plt.subplot(111)
#:TODO plot wells


    
ax2 = plt.subplot(111)
lon_0, lat_0 = .5*( dPar['xmin']+dPar['xmax']), .5*( dPar['ymin']+dPar['ymax'])
m = Basemap(llcrnrlon = dPar['xmin'], urcrnrlon=dPar['xmax'],
            llcrnrlat = dPar['ymin'], urcrnrlat=dPar['ymax'],
            projection=dPar['projection'], lon_0 = lon_0, lat_0 = lat_0)

lon=mSeis[1]
lat=mSeis[2]
    
x,y = m(lon, lat)
m.plot(x, y, 'r.')
         
plt.show()
#ax1.plot(lon, lat, 'g-')

print("Please click %i times"%( dPar['nClicks']))
tCoord = plt.ginput( dPar['nClicks'])
print("clicked", tCoord)
plt.show()

aLon =  np.array( tCoord).T[0]
aLat =  np.array( tCoord).T[1]



x,y = m(aLon, aLat)
m.plot(x, y, 'g-')
plt.show()
#--------------------------3---------------------------------------------
#               compute affected area
#------------------------------------------------------------------------
#TODO: compute area using eis_utils.area_poly
#A_seis = ???
print('total area affected by seismicity: 20,000km^2')
print('fraction of area of OK: 1/10')



