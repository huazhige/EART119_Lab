# -*- coding: utf-8 -*-
#Cesar Laguna
#Python 3.6

import numpy as np
import os
#from __future__ import division
import matplotlib.pyplot as plt


from mpl_toolkits.basemap import Basemap
import seis_utils
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

#--------------------------1---------------------------------------------
#                        load data
#------------------------------------------------------------------------
#os.chdir( data_dir)
np.array
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

mSeis  = np.array( [aTime, mSeis[7], mSeis[8], mSeis[-1]] )
mWells = np.loadtxt( file_well).T
#--------------------------2---------------------------------------------
#                  earthquake rates, cumulative number
#------------------------------------------------------------------------
eq_total = len(mSeis[0])


# plot rate and cumulative number of events
t0    = float()
k_win = 200
at    = np.array([])
aWell = mWells[1]
x     = sorted(mWells[1])
t0    = aWell[0]
at    = mSeis[0]
#at   -= t0

aV    = np.array([])
aV    = mWells[4]



if dPar['showRate'] == True:
    plt.figure(1)
    ax = plt.subplot(211)
    # compute seismicity rates using seis_utils.eqRate
    aBin, aRate = seis_utils.eqRate(at, k_win)
    
    #TODO: plot seismicity rates
    fig1 = plt.figure(1)
    ax = plt.subplot(211)
    ax.plot(aBin, aRate, 'b-', ms = 2)
    ax.set_ylabel( 'Earthquake Rate [ev/mo]')
    
    ax2 = plt.subplot( 212)
    #TODO: plot cumulative number of earthquakes
    ax2.plot(aWell, aV, 'ro', ms = 2)

    ax2.set_xlabel( 'Time [dec. yr]')
    ax2.set_ylabel('Cumulative Number')
    ax2.set_xlim( ax.get_xlim())
    plt.show()
#--------------------------3---------------------------------------------
#                       map view of well and event locations
#------------------------------------------------------------------------
# create time vector with dt_map spacing
mLoc = np.genfromtxt( file_eq, skip_header = 1, usecols=(7,8,10), dtype = float).T
# sort according to year of occurrence
sort_id = aTime.argsort()
aYr = aTime[sort_id]
mLoc= mLoc.T[sort_id].T
at_bin  = np.arange( dPar['tmin'], 2018, dPar['dt_map'])
for i in range( at_bin.shape[0]-1):
    t1, t2 = at_bin[i], at_bin[i+1]
    #TODO: select earthquakes between t1 and t2 use np.logical_and
    sel_eq = np.logical_and( mSeis[0]  >= t1, mSeis[0]   < t2)
    #TODO: select wells with start dates before t2
    sel_we = np.logical_and(mWells[1]  <= t1, 0)
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
    aX, aY = m(  mLoc[0][sel_eq], mLoc[1][sel_eq])

    #TODO: plot seismicity and well locations
    plt.plot(  aX, aY, 'ro', ms = 2, mew = 1.5, mfc = 'none')
    

    # x and y labels
    m.drawparallels( np.arange( 33,   38,  1), fmt='%i',labels=[1,0,0,0])
    m.drawmeridians( np.arange(-100,  -92, 2), fmt='%i',labels=[0,0,0,1])
    #--------------

    #file_out = 'OK_seis_t_%.1f_%.1f.png'%( t1, t2)
    #plt.savefig(  file_out, dpi = 150)
    #plt.clf()

    plt.pause( .5)
