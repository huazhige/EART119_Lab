# -*- coding: utf-8 -*-
"""

--> 1) load ANSS seismicity data and well locations for Oklahoma
--> 2) plot eq rates
--> 3) plot cumulative rate
--> 4) seismicity and well map in moving time windows

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


showRate = True
dt_map   = 6./12 # time step for plotting eq and wells in map view

             # for rate computations
k        = 200                 
tmin    = 2005 # play with this number to visualize historic rates
             # -----basemap params----------------------
#xmin = -101, xmax = -94
#ymin =   33.5, ymax =  37.1,
#projection = merc # or 'aea' for equal area projections


#--------------------------1---------------------------------------------
#                        load data
#------------------------------------------------------------------------
os.chdir( data_dir)
# load seismicity and well data using loadtxt
mSeis  = np.loadtxt( file_eq, comments = '#').T
#TODO: convert date-time to decimal year using seis_utils.dateTime2decYr
YR = mSeis[1]
MO = mSeis[2]
DY = mSeis[3]
HR = mSeis[4]
MN = mSeis[5]
SC = mSeis[6]
def decYr( YR, MO, DY, HR, MN, SC):
    nDays = 365.25
    return YR + (MO-1)/12 + (DY-1)/nDays  + HR/(nDays*24) + MN/(nDays*24*60) + SC/(nDays*24*3600)
print decYr( YR, MO, DY, HR, MN, SC)
at = decYr( YR, MO, DY, HR, MN, SC)

mSeis  = np.array( [at, mSeis[7], mSeis[8], mSeis[-1]])
mWells = np.loadtxt( file_well).T
#--------------------------2---------------------------------------------
#                  earthquake rates, cumulative number
#------------------------------------------------------------------------

# plot rate and cumulative number of events
#if dPar['showRate'] == True:
    # compute seismicity rates using seis_utils.eqRate
def eqRate( at, k):
    # smoothed rate from overlapping sample windows normalized by delta_t
        aS          = np.arange( 0, at.shape[0]-k, 1)
        aBin, aRate = np.zeros(aS.shape[0]), np.zeros(aS.shape[0])
        iS = 0
        for s in aS:
            i1, i2 = s, s+k
            aBin[iS]  = 0.5*( at[i1]+at[i2])
            aRate[iS] = k/( at[i2]-at[i1])
            iS += 1
        return aBin, aRate
aBin, aRate = eqRate( at, k)
#print aBin, aRate
    #TODO: plot seismicity rates
plt.figure(1)
ax1 = plt.subplot( 211)
ax1.plot( aBin, aRate, 'r-')
ax1.set_xlabel( 'Time [dec. yr]')

ax1.set_ylabel( 'Earthquake Rate [ev/mo]')
ax2 = plt.subplot( 212)
    
    #TODO: plot cumulative number of earthquakes
with open(file_eq) as f:
    N = (sum(1 for _ in f) - 1) #-1 accounts for header
sumEq = np.cumsum( np.ones( N))
ax2.plot( at, sumEq, 'b-')

ax2.set_xlabel( 'Time [dec. yr]')
ax2.set_ylabel('Cumulative Number')
ax2.set_xlim( ax1.get_xlim())
plt.show()

"""
#--------------------------3---------------------------------------------
#                       map view of well and event locations
#------------------------------------------------------------------------
# create time vector with dt_map spacing
at_bin  = np.arange( dPar['tmin'], 2018, dPar['dt_map'])
for i in range( at_bin.shape[0]-1):
    t1, t2 = at_bin[i], at_bin[i+1]
    #TODO: select earthquakes between t1 and t2 use np.logical_and
    sel_eq = np.logical_and( mSeis[0]  >= t1, mSeis[0]   < t2)
    #TODO: select wells with start dates before t1
    ???
    print t1, t2, 'No. earthquakes', sel_eq.sum(), 'No. of wells', sel_we.sum()
    ### create basemap object
    plt.figure(2)
    plt.cla()
    ax2 = plt.subplot(111)
    lon_0, lat_0 = .5*( dPar['xmin']+dPar['xmax']), .5*( dPar['ymin']+dPar['ymax'])
    m = Basemap(llcrnrlon = dPar['xmin'], urcrnrlon=dPar['xmax'],
                llcrnrlat = dPar['ymin'], urcrnrlat=dPar['ymax'],
                lon_0 = lon_0, lat_0 = lat_0
                resolution = 'l',
                projection=dPar['projection'], )
    #TODO: draw state boundaries
        lon_0, lat_0 = .5*( xmin + xmax), .5*( ymin + ymax)
    m = Basemap(projection = 'cyl',
                llcrnrlon = xmin, urcrnrlon=xmax,
                llcrnrlat = ymin, urcrnrlat=ymax,
                 resolution = 'c', lon_0 = lon_0, lat_0 = lat_0)
    m.drawcoastlines()
    aX_eq, aY_eq = m(  mLoc[0][sel_eq], mLoc[1][sel_eq])
    ???

    #TODO: convert spherical to 2D coordinate system using basemap
    ???
    ???

    # TODO: plot seismicity and well locations
    ???
    ???

    # x and y labels
    m.drawparallels( np.arange( 33,   38,  1), fmt='%i',labels=[1,0,0,0])
    m.drawmeridians( np.arange(-100,  -92, 2), fmt='%i',labels=[0,0,0,1])
    #--------------

    #file_out = 'OK_seis_t_%.1f_%.1f.png'%( t1, t2)
    #plt.savefig(  file_out, dpi = 150)
    #plt.clf()

    plt.pause( .5)

"""

#--------------------------4---------------------------------------------
#                  insight from rate plots (part e)
#------------------------------------------------------------------------
"""
From looking at the earthquake rates, the rates begins to spike significantly 
between 2010 and 2015. The earthquake rate rapidly increases for a few years
until gradually declining after a peak in rates around 2015. I suspect the 
earthquake rate picked up at the time that it did because underground injections
started to take effect on the crust and it started to decline after the injections
ceased or slowed. 
"""







