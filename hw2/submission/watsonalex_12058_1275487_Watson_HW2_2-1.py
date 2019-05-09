#!/bin/python2.7
"""
HW2 Part 2 - Alex Watson
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
import Modules.seis_utils as seis_utils
#--------------------------0---------------------------------------------
#                     params, dirs, files
#------------------------------------------------------------------------
data_dir   = 'Data'
file_eq    = 'seism_OK.txt'
file_well  = 'injWell_OK.txt'

dPar  =  {   'nClicks' : 10,
             'tmin'    : 2011,
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
aTime  = seis_utils.dateTime2decYr( mSeis[1], mSeis[2], mSeis[3], mSeis[4], mSeis[5], mSeis[6])
mSeis  = np.array( [aTime, mSeis[7], mSeis[8], mSeis[-1]])
#TODO: select most recent seismic events
sel    = mSeis[0] >= dPar['tmin']
mSeis  = mSeis.T[sel].T
mWells = np.loadtxt( file_well).T

#--------------------------2---------------------------------------------
#                       map view, select boundaries of seismicity
#------------------------------------------------------------------------
plt.figure(1)
ax1 = plt.subplot(111)
#:TODO plot wells
aX_we, aY_we = mWells[2], mWells[3]
plot_we = plt.scatter( aX_we, aY_we, c = 'b', s = 1.0)
#:TODO plot seismicity
aX_eq, aY_eq = mSeis[1], mSeis[2]
plot_eq = plt.scatter( aX_eq, aY_eq, c = 'r')
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
aX, aY = m(aLon, aLat)
plt.plot(aX, aY)



#--------------------------3---------------------------------------------
#               compute affected area
#------------------------------------------------------------------------
#TODO: compute area using seis_utils.area_poly
A_seis = seis_utils.area_poly(aLon*111, aLat*111)
print 'total area affected by seismicity: ', A_seis
print 'fraction of area of OK', A_seis/(dPar['areaOK']) # about 1/3







