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
os.chdir( data_dir)
# load seismicity and well data using loadtxt
mSeis  = np.loadtxt( file_eq).T

#:TODO data-time to decimal years
aYr = np.genfromtxt( mSeis, skip_header = 1, usecols=(1), delimiter=' ', dtype = int)
MO = np.genfromtxt( mSeis, skip_header = 1, usecols=(2), delimiter=' ', dtype = int)
DY = np.genfromtxt( mSeis, skip_header = 1, usecols=(3), delimiter=' ', dtype = int)
HR = np.genfromtxt( mSeis, skip_header = 1, usecols=(4), delimiter=' ', dtype = int)
MN = np.genfromtxt( mSeis, skip_header = 1, usecols=(5), delimiter=' ', dtype = int)
SC = np.genfromtxt( mSeis, skip_header = 1, usecols=(6), delimiter=' ', dtype = int)

aTime  = seis_utils.dateTime2decYr( YR, MO, DY, HR, MN, SC)
mSeis  = np.array( [aTime, mSeis[7], mSeis[8], mSeis[-1]])

#TODO: select most recent seismic events
at_bin  = np.arange( dPar['tmin'])
sel = np.logical_and( mSeis[0]  >= at_bin )
mSeis  = mSeis.T[sel].T
mWells = np.loadtxt( file_well).T

#--------------------------2---------------------------------------------
#                       map view, select boundaries of seismicity
#------------------------------------------------------------------------
plt.figure(1)
ax1 = plt.subplot(111)
#:TODO plot wells
#:TODO plot seismicity
ax_eq, aY_eq = m(  mSeis[7], mSeis[8])
    ax1.plot (as_eq, aY_eq, 'b-')
    xWell, yWell = m( mWells[3], mWells[4])
    ax2.plot (xWell, yWell, 'ko')

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
???


#--------------------------3---------------------------------------------
#               compute affected area
#------------------------------------------------------------------------
#TODO: compute area using eis_utils.area_poly
xWell = np.genfromtxt( mWells, skip_header = 1, usecols=(3), delimiter=' ', dtype = int)
yWell = np.genfromtxt( mWells, skip_header = 1, usecols=(4), delimiter=' ', dtype = int)
A_seis = seis_utils.area_poly(xWell, yWell)
print 'total area affected by seismicity: ', A_seis
print 'fraction of area of OK', A_seis/(dPar['areaOK']) # about 1/3







