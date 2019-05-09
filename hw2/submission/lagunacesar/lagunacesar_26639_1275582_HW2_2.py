# -*- coding: utf-8 -*-
#Cesar Laguna
#Python 3.6

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
import seis_utils
#--------------------------0---------------------------------------------
#                     params, dirs, files
#------------------------------------------------------------------------
data_dir   = './'
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
#TODO: convert date-time to decimal year use seis_utils.dateTime2decYr
YR = np.array([])
M0 = np.array([])
DY = np.array([])
HR = np.array([])
MN = np.array([])
SC = np.array([])
YR, MO, DY, HR, MN, SC = mSeis[1], mSeis[2], mSeis[3], mSeis[4], mSeis[5], mSeis[6]
DecYear = YR + (MO-1)/12 + (DY-1)/365.25+ HR/(365.25*24) + MN/(365.25*24*60) + SC/(365.25*24*3600)

aTime = DecYear

mSeis  = np.array( [aTime, mSeis[7], mSeis[8], mSeis[-1]])

#TODO: select most recent seismic events
sel    = mSeis > 2016
mSeis  = mSeis[sel].T
mWells = np.loadtxt( file_well).T

#--------------------------2---------------------------------------------
#                       map view, select boundaries of seismicity
#------------------------------------------------------------------------
plt.figure(1)
ax1 = plt.subplot(111)
#:TODO plot wells
t0 = np.array([])
mV = np.array([])
t0 = mWells[1]
mV = mWells[4]
time = mSeis[0]
mag  = mSeis[3]
ax1.plot(t0, mV , 'bo', ms = 2)


#:TODO plot seismicity
ax2 = plt.subplot( 111)
ax2.plot(time, mag, 'r-', ms = 2)
print("Please click %i times"%( dPar['nClicks']))
tCoord = plt.ginput( dPar['nClicks'])
print("clicked", tCoord)
plt.show()

aLon =  np.array( tCoord).T[0]
aLat =  np.array( tCoord).T[1]


# project into equal area coordinate system
mLoc = np.genfromtxt( file_eq, skip_header = 1, usecols=(7,8,10), dtype = float).T
# sort according to year of occurrence
sort_id = aTime.argsort()
aYr = aTime[sort_id]
mLoc= mLoc.T[sort_id].T


lon_0, lat_0 = .5*( dPar['xmin']+dPar['xmax']), .5*( dPar['ymin']+dPar['ymax'])
m = Basemap(llcrnrlon = dPar['xmin'], urcrnrlon=dPar['xmax'],
            llcrnrlat = dPar['ymin'], urcrnrlat=dPar['ymax'],
            projection=dPar['projection'], lon_0 = lon_0, lat_0 = lat_0)

m.drawcoastlines()
m.drawcountries()

#TODO: project into equal area coordinate system

aX, aY = m(  mLoc[0][sel_eq], mLoc[1][sel_eq])
plt.plot(  aX, aY, 'ro', ms = 2, mew = 1.5, mfc = 'none')

#--------------------------3---------------------------------------------
#               compute affected area
#------------------------------------------------------------------------
#TODO: compute area using eis_utils.area_poly
A_seis = seis_utils.area_poly()
print ('total area affected by seismicity: ', A_seis)
print ('fraction of area of OK', A_seis/(dPar['areaOK'])) # about 1/3

