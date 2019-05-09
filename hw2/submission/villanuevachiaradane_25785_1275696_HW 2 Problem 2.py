#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/bin/python2.7
"""

--> 1) load OK seismicity and well data
--> 2) plot eqs and wells using matplotlib
--> 3) select polygon that encompasses seism., project to equal area
       and compute area of polygon



"""
from __future__ import division
import os
import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.basemap import Basemap

#------------my modules-----------------------
import modules.seis_utils as seis_utils
#--------------------------0---------------------------------------------
#                     params, dirs, files
#------------------------------------------------------------------------
data_dir   = /Data
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
os.chdir( data_dir)
# load seismicity and well data using loadtxt
mSeis  = np.loadtxt( file_eq).T
#:TODO data-time to decimal years
aTime  = seis_utils.dateTime2decYr(mSeis[1], mSeis[2], mSeis[3], mSeis[4], mSeis[5], mSeis[6])
mSeis  = np.array( [aTime, mSeis[7], mSeis[8], mSeis[-1]])
#TODO: select most recent seismic events
sel    = np.logical_and( mSeis[0]  >= t1, mSeis[0]   < t2)
mSeis  = mSeis.T[sel].T
mWells = np.loadtxt( file_well).T

#--------------------------2---------------------------------------------
#                       map view, select boundaries of seismicity
#------------------------------------------------------------------------
plt.figure(1)
ax1 = plt.subplot(111)
#:TODO plot wells & seismicity
mLoc = np.genfromtxt(file_eq, skip_header = 1, usecols = (7, 8, 10), dtype = float).T
sort_id = aTime.argsort()
aYr = aTime[sort_id]
mLoc = mLoc.T[sort_id].T
sel_eq = np.logical_and( mSeis[0]  >= t1, mSeis[0]   < t2)
aX, aY = m(mLoc[0][sel_eq], mLoc[1][sel_eq])
plt.plot(aX, aY, 'ro', ms = 2, mew = 1.5, mfc = 'none')

print("Please click %i times"%( dPar['nClicks']))
tCoord = plt.ginput( dPar['nClicks'])
print("clicked", tCoord)
plt.show()

aLon =  np.array( tCoord).T[0]
aLat =  np.array( tCoord).T[1]


# project into equal area coordinate system
lon_0, lat_0 = .5*( dPar['xmin']+dPar['xmax']), .5*( dPar['ymin']+dPar['ymax'])
m = Basemap(llcrnrlon = dPar['xmin'], urcrnrlon=dPar['xmax'],
            llcrnrlat = dPar['ymin'], urcrnrlat=dPar['ymax'],
            projection=dPar['projection'], lon_0 = lon_0, lat_0 = lat_0)
#TODO: project into equal area coordinate system
m.drawstates()
m.drawparallels( np.arange( 33,   38,  1), fmt='%i',labels=[1,0,0,0])
m.drawmeridians( np.arange(-100,  -92, 2), fmt='%i',labels=[0,0,0,1])
ax = plt.gca()
for y in np.linspace(m.ymax/20,19*m.ymax/20,10):
    for x in np.linspace(m.xmax/20,19*m.xmax/20,12):
        lon, lat = m(x,y,inverse=True)
        poly = m.tissot(lon,lat,1.25,100,                        facecolor='green',zorder=10,alpha=0.5)
plt.show()

#--------------------------3---------------------------------------------
#               compute affected area
#------------------------------------------------------------------------
#TODO: compute area using eis_utils.area_poly
A_seis = seis_utils.area_poly(aX, aY)
print 'total area affected by seismicity: ', A_seis
print 'fraction of area of OK', A_seis/(dPar['areaOK']) # about 1/3

