#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 20:21:11 2019

@author: williamdean
"""
import os
from _future_ import divison
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.basemap import Basemap
import pandas as pd

#files, params, dirs
data_dir = '/Users/williamdean/Documents/GitHub/EART119'
file_eq    = 'seism_OK.txt'
file_well  = 'injWell_OK.txt'
dPar  =  {   'nClicks' : 10,'tmin'    : 2010,'areaOK'  : 181*1e3, #in km
          # -----basemap params----------------------
          'xmin' : -101, 'xmax' : -94,
          'ymin' :   33.5, 'ymax' :  37.1,
          'projection' : 'aea',
          # or 'cea' 'aea' for equal area projections
          }

#load data

os.chdir( data_dir)
mSeis  = np.loadtxt( file_eq).T

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
    return YR + (MO-1)/12 + (DY-1)/nDays  + HR/(nDays*24) + MN/(nDays*24*60) 
    + SC/(nDays*24*3600)
aTime = 100
mSeis  = np.array( [aTime, mSeis[7], mSeis[8], mSeis[-1]])
sel = 2017
mSeis  = mSeis.T[sel].T
mWells = np.loadtxt( file_well).T

#plot
plt.figure(1)
ax1 = plt.subplot(111)

plt.plot( file_eq)
plt.plot( file_well)

print("Please click %i times"%( dPar['nClicks']))
tCoord = plt.ginput( dPar['nClicks'])
print("clicked", tCoord)
plt.show()
aLon =  np.array( tCoord).T[0]
aLat =  np.array( tCoord).T[1]

lon_0, lat_0 = .5*( dPar['xmin']+dPar['xmax']), .5*( dPar['ymin']+dPar['ymax'])
m = Basemap(llcrnrlon = dPar['xmin'], urcrnrlon=dPar['xmax'],
            llcrnrlat = dPar['ymin'], urcrnrlat=dPar['ymax'],
            projection=dPar['projection'], lon_0 = lon_0, lat_0 = lat_0)

def area_poly( aX, aY): 

     
    A = 0.1*abs( (x1*y2 + x2*y3 + xn-1*yn + xn*y1) - (y1*x2 + y2*x3 + ... + yn-1*xn + yn*x1))
    :param aX: - x-coordinates of all vertices
    :param aY: - y-coordinates of all vertices
    :return: A - 'area of polygon'

    #sumVert1 = (aX[0:-1]*aY[1::]).sum()+aX[-1]*aY[0]
    # or:
sumVert1  = np.dot( aX[0:-1], aY[1::])+aX[-1]*aY[0]
    #sumVert2 = (aY[0:-1]*aX[1::]).sum()+aY[-1]*aX[0]
    # or:
sumVert2  = np.dot(aY[0:-1], aX[1::])+aY[-1]*aX[0]
    #sum = (aX[0:-1]*aY[1::] - aY[0:-1]*aX[1::]).sum() + (aX[-1]*aY[0]-aY[-1]*aX[0])
return 0.5*abs( sumVert1 - sumVert2)

print 'total area affected by seismicity: ', mSeis
print 'fraction of area of OK', mSeis/(dPar['areaOK'])
