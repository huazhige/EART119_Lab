#!/bin/python2.7
"""

--> 1) load ANSS seismicity data and well locations for Oklahoma
--> 2) plot eq rates
--> 3) plot cumulative rate
--> 4) seismicity and well map in moving time windows



"""
from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.basemap import Basemap

#------------my modules-----------------------
#import module.seis_utils 
#--------------------------0---------------------------------------------
#                     params, dirs, files
#------------------------------------------------------------------------
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
mWells = np.loadtxt( file_well).T
#---------------------------------------------------------------------decyear
#TODO: convert date-time to decimal year use seis_utils.dateTime2decYr
def dateTime2decYr( YR, MO, DY, HR, MN, SC):
    """
    - convert date time to decimal year
    :param YR: - int or arrays
    :param MO:
    :param DY:
    :param HR:
    :param MN:
    :param SC:
    :return:
    """
    nDays = 365.25
    return YR + (MO-1)/12 + (DY-1)/nDays  + HR/(nDays*24) + MN/(nDays*24*60) + SC/(nDays*24*3600)
#---------------------------------------------------------------------
    
aTime = dateTime2decYr(mSeis[1], mSeis[2], mSeis[3], mSeis[4], mSeis[5], mSeis[6])

mSeis  = np.array( [aTime, mSeis[7], mSeis[8], mSeis[-1]])

#--------------------------2---------------------------------------------
#                  earthquake rates, cumulative number
#------------------------------------------------------------------------

# plot rate and cumulative number of events

#---------------------------------------------------------------------rate
k_win = 200
    # compute seismicity rates using seis_utils.eqRate    
def eqRate( at, k_win):
    # smoothed rate from overlapping sample windows normalized by delta_t
    aS          = np.arange( 0, at.shape[0]-k_win, 1)
    aBin, aRate = np.zeros(aS.shape[0]), np.zeros(aS.shape[0])
    iS = 0
    for s in aS:
        i1, i2 = s, s+k_win
        aBin[iS]  = 0.5*( at[i1]+at[i2])
        aRate[iS] = k_win/( at[i2]-at[i1])
        iS += 1
    return aBin, aRate
#---------------------------------------------------------------------
    

rate = eqRate(aTime, k_win)  
L = np.cumsum( np.ones( len(aTime)))

#---------------------------------------------------------------------plot 1
#TODO: plot seismicity rates
if dPar['showRate'] == True:
    plt.figure(1)
    ax = plt.subplot( 211)
  
    ax.hist(aTime, k_win)
    ax.set_ylabel( 'Earthquake Rate [ev/mo]')
#---------------------------------------------------------------------
    
#---------------------------------------------------------------------plot 2
    #TODO: plot cumulative number of earthquakes

    ax2 = plt.subplot( 212)
    ax2.plot(aTime, L)
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
    #TODO: select wells with start dates before t2
    sel_we = np.logical_and(mWells[1]  >= t1, mWells[1]   < t2)
    
    print t1, t2, 'No. earthquakes', sel_eq.sum(), 'No. of wells', sel_we.sum()
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
    m.drawstates(linewidth=0.5)

    #TODO: convert spherical to 2D coordinate system using basemap
    aX_eq, aY_eq = m(  mSeis[1][sel_eq], mSeis[2][sel_eq])

    # TODO: plot seismicity and well locations
    plot1 =     plt.scatter( aX_eq, aY_eq, c = mSeis[3][sel_eq], s = np.exp( mSeis[3][sel_eq]))
    
    if i ==0:
        cbar  = plt.colorbar( plot1, orientation = 'horizontal')
        cbar.set_label( 'Magnitude')
        
        
    # x and y labels
    m.drawparallels( np.arange( 33,   38,  1), fmt='%i',labels=[1,0,0,0])
    m.drawmeridians( np.arange(-100,  -92, 2), fmt='%i',labels=[0,0,0,1])
    #--------------
    
    #file_out = 'OK_seis_t_%.1f_%.1f.png'%( t1, t2)
    #plt.savefig(  file_out, dpi = 150)
    #plt.clf()
    
    plt.pause( .05)





"""
e) From your analysis of earthquake rates and locations, in what year did seismicity rates
start to significantly exceed historic values? When did earthquake rates start to again
decrease? Can you speculate on why?

Rates began to climb around 2010, and decreased again by 2016. 
This is most likely due to the induced earthquakes by the pressure wells. 




"""





