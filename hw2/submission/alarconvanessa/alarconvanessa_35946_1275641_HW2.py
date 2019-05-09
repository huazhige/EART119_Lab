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
#data_dir   = ???
seismographData    = 'seism_OK.txt'
injWell  = 'injWell_OK.txt'


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
mSeis  = np.loadtxt( seismographData).T
mWell  = np.loadtxt( injWell).T
#TODO: convert date-time to decimal year use seis_utils.dateTime2decYr
seisYear  = np.genfromtxt( seismographData, skip_header = 1, usecols=(1), 
                          delimiter='  ', dtype = int)
seisMonth = np.genfromtxt( seismographData, skip_header = 1, usecols =(2),
                          delimiter='  ', dtype = int)
seisDay = np.genfromtxt( seismographData, skip_header = 1, usecols =(3),
                          delimiter='  ', dtype = int)
seisHour = np.genfromtxt( seismographData, skip_header = 1, usecols =(4),
                          delimiter='  ', dtype = int)
seisMin = np.genfromtxt( seismographData, skip_header = 1, usecols =(5),
                          delimiter='  ', dtype = int)
seisSec = np.genfromtxt( seismographData, skip_header = 1, usecols =(6),
                          delimiter='  ', dtype = int)

#//////////////////////////////////////////////////////////////////////////////
#                           Dec Year function
#//////////////////////////////////////////////////////////////////////////////


def decimalYear(Yr, Mo, Day, Hour, Min, Sec):
    DecYear = Yr + (Mo-1)/12 + (Day-1)/365.25+ Hour/(365.25*24) + Min/(365.25*24*60) + Sec/(365.25*24*3600)
    return DecYear

aTime = decimalYear(seisYear, seisMonth, seisDay, seisHour, seisMin, seisSec)


mSeis  = np.array( [aTime, mSeis[7], mSeis[8], mSeis[-1]])
mWells = np.loadtxt( injWell).T
#--------------------------2---------------------------------------------
#                  earthquake rates, cumulative number
#------------------------------------------------------------------------
def compRate(at, k): # compute the rate of change for time vector at
    """input
            at  - time vector
            k   - sample window - controls smoothness
        output  aBin, aRate
    """
    aS = np.arange( 0, at.shape[0] - k, 1)
    aBin = np.zeros(aS.shape[0])
    aRate = np.zeros(aS.shape[0])
    iS = 0
    for sStep in aS:
        i1, i2 = sStep, sStep + k
        aRate = k/(at[i2] - at[i1])
        aBin[iS] = (at[i1] + at[i2])/2
        
        iS += 1
        return aBin, aRate
# plot rate and cumulative number of events
if dPar['showRate'] == True:
    plt.figure(1)
    ax = plt.subplot( 211)
    aBin, aRate = compRate( mSeis[0], 200)
   
    #TODO: plot seismicity rates

    
    ax.set_ylabel( 'Earthquake Rate [ev/mo]')
    ax2 = plt.subplot( 212)
    #TODO: plot cumulative number of earthquakes
    
   # for i in range( at_bin.shape[0]-1):
  #  t1, t2 = at_bin[i], at_bin[i+1]
   
 #   sel_eq = np.logical_and( mSeis[0]  >= t1)

    

    ax2.set_xlabel( 'Time [dec. yr]')
    ax2.set_ylabel('Cumulative Number')
    ax2.set_xlim( ax.get_xlim())
    plt.show()


#--------------------------3---------------------------------------------
#                       map view of well and event locations
#------------------------------------------------------------------------
# create time vector with dt_map spacing
at_bin  = np.arange( dPar['tmin'], 2018, dPar['dt_map'])
#print(at_bin)

for i in range( at_bin.shape[0]-1):
    t1, t2 = at_bin[i], at_bin[i+1]
    #TODO: select earthquakes between t1 and t2 use np.logical_and
    sel_eq = np.logical_and( mSeis[0]  >= t1, mSeis[0]   < t2)
    sel_we = np.logical_not( mWell[1] >= t1 )
    #TODO: select wells with start dates before t1
   
    print (t1, t2, 'No. earthquakes', sel_eq.sum(), 'No. of wells', sel_we.sum())
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
    #TODO: draw state boundaries
 
    m.drawstates()
    #TODO: convert spherical to 2D coordinate system using basemap
    S_xpt, S_ypt = m(mSeis[1], mSeis[2])
    W_xpt, W_ypt = m(mWell[2], mWell[3])
   

    # TODO: plot seismicity and well locations
    m.plot(S_xpt, S_ypt, 'bo')
    m.plot(W_xpt, W_ypt, 'ro')
    

    # x and y labels
    m.drawparallels( np.arange( 33,   38,  1), fmt='%i',labels=[1,0,0,0])
    m.drawmeridians( np.arange(-100,  -92, 2), fmt='%i',labels=[0,0,0,1])
    #--------------

    #file_out = 'OK_seis_t_%.1f_%.1f.png'%( t1, t2)
    #plt.savefig(  file_out, dpi = 150)
    #plt.clf()

    plt.pause( .5)













