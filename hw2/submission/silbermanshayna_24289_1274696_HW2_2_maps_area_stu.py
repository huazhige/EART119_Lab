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
import seis_utils
#--------------------------0---------------------------------------------
#                     params, dirs, files
#------------------------------------------------------------------------
data_dir   = 'X:\EARTH119_test'
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
#os.chdir( data_dir)
# load seismicity and well data using loadtxt
mSeis  = np.loadtxt( file_eq).T
# data-time to decimal years
aTime  = np.array([])

for n in range( 0, len(mSeis[1])):
   aTime = np.append(aTime, seis_utils.dateTime2decYr(mSeis[1][n], mSeis[2][n], mSeis[3][n],mSeis[4][n], mSeis[5][n], mSeis[6][n]))

mSeis  = np.array( [aTime, mSeis[7], mSeis[8], mSeis[-1]])
# select most recent seismic events
sel = np.logical_and( mSeis[1] < t1, mSeis <t1)

mSeis  = mSeis[sel].T
mWells = np.loadtxt( file_well).T

#--------------------------2---------------------------------------------
#                       map view, select boundaries of seismicity
#------------------------------------------------------------------------
plt.figure(1)
ax1 = plt.subplot(111)
lon_0, lat_0 = .5*( dPar['xmin']+dPar['xmax']), .5*( dPar['ymin']+dPar['ymax'])
    
m = Basemap(llcrnrlon = dPar['xmin'], urcrnrlon=dPar['xmax'],
                llcrnrlat = dPar['ymin'], urcrnrlat=dPar['ymax'],
                lon_0 = lon_0, lat_0 = lat_0,
                resolution = 'l',
                projection=dPar['projection'], )
m.drawstates()
xpt, ypt = m(mSeis[1], mSeis[2])
xpt2, ypt2 = m(mWells[2], mWells[3])
# plot wells
for k in range( 0, len(mWells[1])):
    if(mWells[k].all):
        ax2.plot(xpt2[k], ypt2[k], 'bo')
# plot seismicity
for j in range(0, len(sel)):
    if(sel[j]):
        ax2.plot(xpt[j], ypt[j],'ro')
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



#--------------------------3---------------------------------------------
#               compute affected area
#------------------------------------------------------------------------
# compute area using eis_utils.area_poly

A_seis = np.array([])
for n in range( 0, len(mSeis[1])):
    A_seis = np.append( A_seis, seis_utils.area_poly(mSeis[1][n], mSeis[2][n])
print( 'total area affected by seismicity: ', A_seis)
print( 'fraction of area of OK', A_seis/(dPar['areaOK'])) # about 1/3







