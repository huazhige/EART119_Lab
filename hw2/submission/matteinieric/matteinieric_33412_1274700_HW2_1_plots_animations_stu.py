#!/bin/python2.7
"""

--> 1) load ANSS seismicity data and well locations for Oklahoma
--> 2) plot eq rates
--> 3) plot cumulative rate
--> 4) seismicity and well map in moving time windows



"""
#from __future__ import division
#import os
import matplotlib.pyplot as plt
#from matplotlib
import numpy as np

#from mpl_toolkits.basemap import Basemap

#------------my modules-----------------------
#import seis_utils
#--------------------------0---------------------------------------------
#                     params, dirs, files
#------------------------------------------------------------------------
#data_dir   = ???
#Seis_Data   = 'seism_OK.txt'
#Well_Data  = 'injWell_OK.txt'


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
Well_data = "injWell_OK.txt"
Seismic_data = "seism_OK.txt"
S_D = np.loadtxt(Seismic_data).T
W_D = np.loadtxt(Well_data).T

YR = S_D[1]
MO = S_D[2]
DY = S_D[3]
HR = S_D[4]
MN = S_D[5]
SC = S_D[6]
#os.chdir( data_dir)
# load seismicity and well data using loadtxt
#mSeis  = np.loadtxt( file_seis).T
#TODO: convert date-time to decimal year use seis_utils.dateTime2decYr
DecYear = YR + (MO-1)/12 + (DY-1)/365.25 + HR/(365.25*24) + MN/(365.25*24*60)
+ SC/(365.25*24*3600)

#print (DecYear)
Total_years = ((DecYear[-1]) - (DecYear[0]))
#print (Total_years)
mSeis  = np.array( [DecYear, S_D[7], S_D[8], S_D[-1]])
mWells = np.loadtxt( W_D).T
#--------------------------2---------------------------------------------
#                  earthquake rates, cumulative number
#------------------------------------------------------------------------

# plot rate and cumulative number of events
Num_quakes = len(DecYear)
#print(Num_quakes)
#print(DecYear)

#print(YRS)

#%matplotlib qt
#%matplotlib inline

Total_quakes = np.cumsum(np.ones(Num_quakes))
MONTHS = 12 * Total_years
#%matplotlib inline
#%matplotlib auto
#ax1 = plt.hist(DecYear, normed = True, bins = MONTHS)
#Quake_rate = Num_quakes/(MONTHS)

fig1 = plt.figure(1)
ax1  = plt.subplot(211)
ax1.hist(DecYear, bins = int((Total_years)*12))

#ax2.set_xlabel("Time [dec. yr]")
#ax2.set_ylabel("cumulative number")
ax2  = plt.subplot(212)
ax2  = plt.plot(DecYear, Total_quakes)
plt.show()

"""
Num_quakes = len(DecYear)
if dPar['showRate'] == True:
    plt.figure(1)
    ax = plt.subplot( 211)
    # compute seismicity rates using seis_utils.eqRate

    #TODO: plot seismicity rates
    Quake_rate = Num_quakes/(MONTHS)

    ax.set_ylabel( 'Earthquake Rate [ev/mo]')
    ax2 = plt.subplot( 212)
    #TODO: plot cumulative number of earthquakes
    Total_quakes = np.cumsum( np.ones( Num_quakes))

    ax2.set_xlabel( 'Time [dec. yr]')
    ax2.set_ylabel('Cumulative Number')
    ax2.set_xlim( ax.get_xlim())
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
    sel_we = np.logical_and( mWells[0] >= t1, mWells[0] < t2)
    print(t1, t2, 'No. earthquakes', sel_eq.sum(), 'No. of wells', sel_we.sum())
    ### create basemap object
    plt.figure(2)
    plt.cla()
    ax3 = plt.subplot(111)
    lon_0, lat_0 = .5*( dPar['xmin']+dPar['xmax']), .5*( dPar['ymin']+dPar['ymax'])
    m = Basemap(llcrnrlon = dPar['xmin'], urcrnrlon=dPar['xmax'],
                llcrnrlat = dPar['ymin'], urcrnrlat=dPar['ymax'],
                lon_0 = lon_0, lat_0 = lat_0,
                resolution = 'l',
                projection=dPar['projection'], )
    #TODO: draw state boundaries
    m.drawstates(linewidth=0.5)

    #TODO: convert spherical to 2D coordinate system using basemap
    xpt, ypt = m( mSeis[1][sel_eq], mSeis[2][sel_eq])

    # TODO: plot seismicity and well locations
    ax3 = plt.scatter(xpt_eq, ypt_eq, c = mSeis[3][sel_eq], s = np.exp(mSeis[3][sel_eq])

    if i == 0
        cbar = plt.colorbar( ax3, orientation = "horizontal")
        cbar.set_label( "Magnitude")

    # x and y labels
    m.drawparallels( np.arange( 33,   38,  1), fmt='%i',labels=[1,0,0,0])
    m.drawmeridians( np.arange(-100,  -92, 2), fmt='%i',labels=[0,0,0,1])
    #--------------

    #file_out = 'OK_seis_t_%.1f_%.1f.png'%( t1, t2)
    #plt.savefig(  file_out, dpi = 150)
    #plt.clf()

    plt.pause( .5)
"""
