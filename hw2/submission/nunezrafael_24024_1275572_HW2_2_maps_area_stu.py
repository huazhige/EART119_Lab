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

#from mpl_toolkits.basemap import Basemap

#------------my modules-----------------------
#import seis_utils
#--------------------------0---------------------------------------------
#                     params, dirs, files
#------------------------------------------------------------------------
data_dir   = '../data'
file_eq    = 'seism_OK.txt'
file_well  = 'injWell_OK.txt' 
nClicks = 10
tmin    = 2010 
areaOK  = 181*1e3,#in km
             # -----basemap params----------------------
#xmin = -101, xmax = -94
#ymin  =   33.5, ymax =  37.1,
#             'projection' : 'aea',# or 'cea' 'aea' for equal area projections

#--------------------------1---------------------------------------------
#                        load data
#------------------------------------------------------------------------
os.chdir( data_dir)
# load seismicity and well data using loadtxt
mSeis  = np.loadtxt( file_eq).T
#:TODO data-time to decimal years
YR = mSeis[1]
MO = mSeis[2]
DY = mSeis[3]
HR = mSeis[4]
MN = mSeis[5]
SC = mSeis[6]
def decYr( YR, MO, DY, HR, MN, SC):
    nDays = 365.25
    return YR + (MO-1)/12 + (DY-1)/nDays  + HR/(nDays*24) + MN/(nDays*24*60) + SC/(nDays*24*3600)
at = decYr( YR, MO, DY, HR, MN, SC)
mSeis  = np.array( [at, mSeis[7], mSeis[8], mSeis[-1]])
#TODO: select most recent seismic events
for t in at:
    if at[t] < at[t+1]:
        t += 1
        if t == len(at):  
            t = 0
        else:
            t = t
    else: 
        t0 = at[t]
    print t0
 

#--------------------------2---------------------------------------------
#                       map view, select boundaries of seismicity
#------------------------------------------------------------------------
plt.figure(1)
ax1 = plt.subplot(111)
#:TODO plot wells
#???
#:TODO plot seismicity
#???
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
#???


#--------------------------3---------------------------------------------
#               compute affected area
#------------------------------------------------------------------------
#TODO: compute area using eis_utils.area_poly
def area_poly( aX, aY):
    aX = xmax - xmin
    aY = ymax - ymin
    sumVert1  = np.dot( aX[0:-1], aY[1::])+aX[-1]*aY[0]
    sumVert2  = np.dot(aY[0:-1], aX[1::])+aY[-1]*aX[0]
A_seis = area_poly
print 'total area affected by seismicity: ', A_seis
print 'fraction of area of OK', A_seis/(dPar['areaOK']) # about 1/3



"""



