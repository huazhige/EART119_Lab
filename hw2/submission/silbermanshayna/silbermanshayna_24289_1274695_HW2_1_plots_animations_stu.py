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
import seis_utils
#--------------------------0---------------------------------------------
#                     params, dirs, files
#------------------------------------------------------------------------
data_dir   = 'X:\EARTH119_test'
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

#--------------------------1---------------------------------------------
#                        load data
#------------------------------------------------------------------------
#os.chdir( data_dir)
# load seismicity and well data using loadtxt
mSeis  = np.loadtxt( file_eq).T
aTime = np.array([])

for n in range( 0, len(mSeis[1])):
   aTime = np.append(aTime, seis_utils.dateTime2decYr(mSeis[1][n], mSeis[2][n], mSeis[3][n],mSeis[4][n], mSeis[5][n], mSeis[6][n]))


mSeis  = np.array( [aTime, mSeis[7], mSeis[8], mSeis[-1]])
mWells = np.loadtxt( file_well).T


#--------------------------2---------------------------------------------
#                  earthquake rates, cumulative number
#------------------------------------------------------------------------

# plot rate and cumulative number of events
if dPar['showRate'] == True:
    plt.figure(1)
    ax = plt.subplot( 211)
    
    seisDataNorm = seis_utils.eqRate(mSeis, 6)
    
    
   # print( seis_utils.eqRate(mSeis, aTime))
    #plot seismicity rates
    plt.figure( 1)
    ax.plot( seisDataNorm[1], seisDataNorm[0],'b-')
    ax.set_xlabel( 'Time [dec. yr]')
    ax.set_ylabel( 'Earthquake Rate [ev/mo]')
    ax2 = plt.subplot( 212)
    #plot cumulative number of earthquakes
    ax2.plot( 0, len(mSeis[1]),'ko')
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
    sel_eq = np.logical_and( mSeis[0]  >= t1, mSeis[0]   < t2)
    #select wells with start dates before t1
   
    # make a list of all wells with start dates before t1
    #We want to find all dates s.t. (if well<t1)
    sel_we = np.logical_and( mWells[1] < t1, mWells <t1)
    
    
    print(t1, t2, 'No. earthquakes', sel_eq.sum(), 'No. of wells', sel_we.sum())
    ### create basemap object
    plt.figure(2)
    plt.cla()
    ax2 = plt.subplot(111)
    lon_0, lat_0 = .5*( dPar['xmin']+dPar['xmax']), .5*( dPar['ymin']+dPar['ymax'])
    
    m = Basemap(llcrnrlon = dPar['xmin'], urcrnrlon=dPar['xmax'],
                llcrnrlat = dPar['ymin'], urcrnrlat=dPar['ymax'],
                lon_0 = lon_0, lat_0 = lat_0,
                resolution = 'l',
                projection=dPar['projection'], )
    #draw state boundaries
    m.drawstates()

    # convert spherical to 2D coordinate system using basemap
    xpt, ypt = m(mSeis[1], mSeis[2])
    xpt2, ypt2 = m(mWells[2], mWells[3])

    # plot seismicity and well locations
    for j in range(0, len(sel_eq)):
        if(sel_eq[j]):
            ax2.plot(xpt[j], ypt[j],'ro')
    for k in range( 0, len(sel_we)):
        if(sel_we[k].all):
            ax2.plot(xpt2[k], ypt2[k], 'bo')

    # x and y labels
    m.drawparallels( np.arange( 33,   38,  1), fmt='%i',labels=[1,0,0,0])
    m.drawmeridians( np.arange(-100,  -92, 2), fmt='%i',labels=[0,0,0,1])
    #--------------

    #file_out = 'OK_seis_t_%.1f_%.1f.png'%( t1, t2)
    #plt.savefig(  file_out, dpi = 150)
    #plt.clf()

    plt.pause( .5)













