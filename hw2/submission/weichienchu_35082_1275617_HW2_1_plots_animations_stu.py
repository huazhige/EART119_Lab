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
#from matplotlib
import numpy as np

from mpl_toolkits.basemap import Basemap

#------------my modules-----------------------
import seis_utils.py
#--------------------------0---------------------------------------------
#                     params, dirs, files
#------------------------------------------------------------------------
data_dir   = '/Users/charity/Desktop/ASTR119'
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
YR  = np.genfromtxt( sData, skip_header = 1, usecols=(1), delimiter=' ', dtype = int)
MO  = np.genfromtxt( sData, skip_header = 1, usecols=(2), delimiter=' ', dtype = int)
DY  = np.genfromtxt( sData, skip_header = 1, usecols=(3), delimiter=' ', dtype = int)
HR  = np.genfromtxt( sData, skip_header = 1, usecols=(4), delimiter=' ', dtype = int)
MN  = np.genfromtxt( sData, skip_header = 1, usecols=(5), delimiter=' ', dtype = int)
SC  = np.genfromtxt( sData, skip_header = 1, usecols=(6), delimiter=' ', dtype = float)
Lon = np.genfromtxt( sData, skip_header = 1, usecols=(7), delimiter=' ', dtype = float)
Lat = np.genfromtxt( sData, skip_header = 1, usecols=(8), delimiter=' ', dtype = float)
Dep = np.genfromtxt( sData, skip_header = 1, usecols=(9), delimiter=' ', dtype = float)
Mag = np.genfromtxt( sData, skip_header = 1, usecols=(10), delimiter=' ', dtype = float)
#--------------------------1---------------------------------------------
#                        load data
#------------------------------------------------------------------------
os.chdir( data_dir)
# load seismicity and well data using loadtxt
mSeis  = np.loadtxt( file_eq).T
#TODO: convert date-time to decimal year use seis_utils.dateTime2decYr
aTime =  seis_utils.dateTime2decYr( YR, MO, DY, HR, MN, SC)

mSeis  = np.array( [aTime, mSeis[7], mSeis[8], mSeis[-1]])
mWells = np.loadtxt( file_well).T
#--------------------------2---------------------------------------------
#                  earthquake rates, cumulative number
#------------------------------------------------------------------------

# plot rate and cumulative number of events
if dPar['showRate'] == True:
    plt.figure(1)
    ax = plt.subplot( 211)
    # compute seismicity rates using seis_utils.eqRate
    seis_utils.eqRate(aTime)
    #TODO: plot seismicity rates
    plt.show()

    ax.set_ylabel( 'Earthquake Rate [ev/mo]')
    ax2 = plt.subplot( 212)
    #TODO: plot cumulative number of earthquakes
    for it in np.unique( YR):
        sel_eq = it == YR
        print( 'current year', it, '#no. of events: ', sel_eq.sum())

    ax2.set_xlabel( 'Time [dec. yr]')
    ax2.set_ylabel('Cumulative Number')
    ax2.set_xlim( ax.get_xlim())
    plt.show()


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
    m.drawcoastlines()
    
    #TODO: draw state boundaries
    m.drawstates()

    #TODO: convert spherical to 2D coordinate system using basemap
    aX_eq, aY_eq = m( mLoc_seis[1][sel_eq], mLoc_seis[2][sel_eq])

    # TODO: plot seismicity and well locations
    plot1 = plt.scatter(aX_eq, aY_eq, c = mLoc_seis[2][sel_eq], s = np.exp( mLoc[2][sel_eq]-3))

    # x and y labels
    m.drawparallels( np.arange( 33,   38,  1), fmt='%i',labels=[1,0,0,0])
    m.drawmeridians( np.arange(-100,  -92, 2), fmt='%i',labels=[0,0,0,1])
    #--------------

    #file_out = 'OK_seis_t_%.1f_%.1f.png'%( t1, t2)
    #plt.savefig(  file_out, dpi = 150)
    #plt.clf()

    plt.pause( .5)













