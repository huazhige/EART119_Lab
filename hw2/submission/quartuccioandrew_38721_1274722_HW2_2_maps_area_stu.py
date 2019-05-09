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
import Modules.seis_utils as seis_utils
#--------------------------0---------------------------------------------
#                     params, dirs, files
#------------------------------------------------------------------------
data_dir   = './Data/'
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
YR  = mSeis[1]
MO  = mSeis[2]
DAY = mSeis[3]
HR  = mSeis[4]
MIN = mSeis[5]
SEC = mSeis[6]
#:TODO data-time to decimal years
aTime  = seis_utils.dateTime2decYr( YR, MO, DAY, HR, MIN, SEC)

mSeis  = np.array( [aTime, mSeis[7], mSeis[8], mSeis[-1]])
#TODO: select most recent seismic events
sel_eq = np.logical_and(mSeis[1] >= dPar['tmin'], mSeis[1] < 2020)
mSeis  = mSeis.T[sel_eq].T
mWells = np.loadtxt( file_well).T

#--------------------------2---------------------------------------------
#                       map view, select boundaries of seismicity
#------------------------------------------------------------------------
plt.figure(1)
ax1 = plt.subplot(111)
#:TODO plot wells
ax1.plot(mWells[2], mWells[3], 'b')
#:TODO plot seismicity
ax2 = plt.subplot( 212)
ax2.plot( mSeis[1], mSeis[2], 'ko')
print("Please click %i times"%( dPar['nClicks']))
tCoord = plt.ginput( dPar['nClicks'])
print("clicked", tCoord)
plt.show()



# project into equal area coordinate system
lon_0, lat_0 = .5*( dPar['xmin']+dPar['xmax']), .5*( dPar['ymin']+dPar['ymax'])
m = Basemap(llcrnrlon = dPar['xmin'], urcrnrlon=dPar['xmax'],
            llcrnrlat = dPar['ymin'], urcrnrlat=dPar['ymax'],
            projection=dPar['projection'], lon_0 = lon_0, lat_0 = lat_0)
#TODO: project into equal area coordinate system
m.drawcoastlines()
mLoc_Seis = np.genfromtxt( file_eq, skip_header = 1, usecols=(7,8), delimiter=' ', dtype = float).T
aX_eq, aY_eq = m(  mLoc_Seis[0][sel_eq], mLoc_Seis[1][sel_eq])



#--------------------------3---------------------------------------------
#               compute affected area
#------------------------------------------------------------------------
#TODO: compute area using eis_utils.area_poly
A_seis = seis_utils.area_poly((dPar['xmax']-dPar['xmin']), (dPar['ymax']-dPar['ymin']))
print 'total area affected by seismicity: ', A_seis
print 'fraction of area of OK', A_seis/(dPar['areaOK']) # about 1/3







