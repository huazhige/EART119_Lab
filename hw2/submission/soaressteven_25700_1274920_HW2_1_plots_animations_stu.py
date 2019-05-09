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
import seis_utils as seis_utils
#--------------------------0---------------------------------------------
#                     params, dirs, files
#------------------------------------------------------------------------
# file_eq    = 'seism_OK.txt'
# file_well  = 'injWell_OK.txt'
file_eq = 'E:/ASTR_119/seism_OK.txt'
file_well = 'E:/ASTR_119/injWell_OK.txt'


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
os.chdir(file_eq)
os.chdir(file_well)
# load seismicity and well data using loadtxt
mSeis  = np.loadtxt( file_eq).T

aTime = seis_utils.dateTime2decYr(mseis[1],mseis[2],mseis[3],mseis[4],mseis[5],mseis[6])
print(aTime)

# =============================================================================

# This is what I had for part b of question 1 before lecture on April 22

# DecYear1 = np.array([])
# DecYear2 = np.array([])
# 
# # YR = seismData[1]
# # MO = seismData[2]
# # DY = seismData[3]
# # HR = seismData[4]
# # MN = seismData[5]
# # SC = seismData[6]
# 
# DecYear1 = well[3]
# 
# for i in range(0,len(seismData[0]),1):
#     DecYear2[i] = (float(seismData[1,i]) + ((float(seismData[2,i]) - 1.)/12.)\
#     + ((float(seismData[3,i]) - 1.)/(365.25)) + \
#     (float(seismData[4,i])/(365.25*24.)) + \
#     (float(seismData[5,i])/(365.25*24.*60.)) + \
#     (float(seismData[6,i])/(365.25*24.*3600.)))
#     i += 1
# 
# print(DecYear2)
# =============================================================================

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
    ???
    #TODO: plot seismicity rates
    ???

    ax.set_ylabel( 'Earthquake Rate [ev/mo]')
    ax2 = plt.subplot( 212)
    #TODO: plot cumulative number of earthquakes
    ???

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
    #TODO: draw state boundaries
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













