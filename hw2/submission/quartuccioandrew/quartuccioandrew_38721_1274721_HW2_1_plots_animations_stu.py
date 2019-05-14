#!/bin/python2.7
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

from mpl_toolkits.basemap import Basemap

#------------my modules-----------------------
import seis_utils as seis_utils
#------------------------------------------------------------------------
#                     params, dirs, files
#------------------------------------------------------------------------
data_dir   = './'
file_eq    = 'seism_OK.txt'
file_well  = 'injWell_OK.txt'


dPar  =  {  'showRate'  : True,
            'dt_map'    : 6./12, # time step for plotting eq and wells in map view

             # for rate computations
             'k'         : 200,

             'tmin'      : 2005, # play with this number to visualize historic rates
             # -----basemap params----------------------
             'xmin' : -101, 'xmax' : -94,
             'ymin' :   33.5, 'ymax' :  37.1,
             'projection' : 'merc',# or 'aea' for equal area projections
           }

#------------------------------------------------------------------------
#                        load data
#------------------------------------------------------------------------
os.chdir( data_dir)
# load seismicity and well data using loadtxt
mSeis  = np.loadtxt( file_eq).T

aTime  = np.array([])
num_Events = len(file_eq)

YR  = mSeis[1]
MO  = mSeis[2]
DAY = mSeis[3]
HR  = mSeis[4]
MIN = mSeis[5]
SEC = mSeis[6]
#TODO: convert date-time to decimal year use seis_utils.dateTime2decYr

aTime = seis_utils.dateTime2decYr( YR, MO, DAY, HR, MIN, SEC)

mLoc_seis  = np.array( [aTime, mSeis[7], mSeis[8], mSeis[-1]])
mWells     = np.loadtxt( file_well).T
mLoc_wells = np.array( [mWells[1], mWells[3], mWells[2]])
#--------------------------2---------------------------------------------
#                  earthquake rates, cumulative number
#------------------------------------------------------------------------

# plot rate and cumulative number of events
if dPar['showRate'] == True:
    plt.figure(1)
    ax1 = plt.subplot( 211)
    # compute seismicity rates using seis_utils.eqRate
    aBin, aRates = seis_utils.eqRate( aTime, dPar.get('k'))
    #TODO: plot seismicity rates
    ax1.plot( aBin, aRates, 'b-')
    
    ax1.set_ylabel( 'Earthquake Rate [ev/mo]')

    ax2 = plt.subplot( 212)
    #TODO: plot cumulative number of earthquakes
    ax2.plot( aTime, mSeis[:,0], 'ko')

    ax2.set_xlabel( 'Time [dec. yr]')
    ax2.set_ylabel('Cumulative Number')
    ax2.set_xlim( ax1.get_xlim())
    plt.show()


#--------------------------3---------------------------------------------
#                       map view of well and event locations
#------------------------------------------------------------------------

xmin, xmax  = -180+1e-4, 180
ymin, ymax  = -90+1e-4, 90


# create time vector with dt_map spacing
at_bin  = np.arange( dPar['tmin'], 2018, dPar['dt_map'])
for i in range( at_bin.shape[0]-1):
    t1, t2 = at_bin[i], at_bin[i+1]
    #TODO: select earthquakes between t1 and t2 use np.logical_and
    sel_eq = np.logical_and( mSeis[0]  >= t1, mSeis[0]   < t2)
    #TODO: select wells with start dates before t1
    sel_we = np.logical_and( mWells[1]  <= t1)
    print(t1, t2, 'No. earthquakes', sel_eq.sum(), 'No. of wells', sel_we.sum())
   
    
    ### create basemap object
    plt.figure(2)
    plt.cla()
    ax2 = plt.subplot(111)
    #plt.title( str( it))
    lon_0, lat_0 = .5*( dPar.xmin + xmax), .5*( ymin + ymax)
    m = Basemap(projection = 'cyl',
                llcrnrlon = xmin, urcrnrlon=xmax,
                llcrnrlat = ymin, urcrnrlat=ymax,
                 resolution = 'c', lon_0 = lon_0, lat_0 = lat_0)
    m.drawcoastlines()

    #TODO: draw state boundaries
    m.drawstates()

    #TODO: convert spherical to 2D coordinate system using basemap
    aX_eq, aY_eq = m(  mLoc_seis[1][sel_eq], mLoc_seis[2][sel_eq])

    # TODO: plot seismicity and well locations
    plot1 =     plt.scatter( aX_eq, aY_eq, c = mLoc_seis[2][sel_eq], s = np.exp( mLoc_seis[2][sel_eq]-3))

    # x and y labels
    m.drawparallels( np.arange( 33,   38,  1), fmt='%i',labels=[1,0,0,0])
    m.drawmeridians( np.arange(-100,  -92, 2), fmt='%i',labels=[0,0,0,1])
    #--------------

    #file_out = 'OK_seis_t_%.1f_%.1f.png'%( t1, t2)
    #plt.savefig(  file_out, dpi = 150)
    #plt.clf()

    plt.pause( .5)
