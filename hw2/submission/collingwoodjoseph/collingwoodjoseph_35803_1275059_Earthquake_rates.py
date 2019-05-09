# -*- coding: utf-8 -*-
"""
Earthquake rates & well locations.
"""

from __future__ import division
import os
import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.basemap import Basemap

import seis_utils

#---------------------DATA DIRECTORY---------------------------
#data_dir = 'C:\\Users\\Joey\\Desktop\\aapython\\Data\\hw2_data'
data_dir = './'
file_eq = 'seism_OK.txt'
file_well = 'injWell_OK.txt'

dPar = {  'showRate' : True,
          'dt_map'   : 6./12, #time step for plotting eq and wells in map view
          #for rate computations
          'k'        : 200,
          'tmin'     : 2005, #play w/ this num to visualize historic rates
          #basemap params
          'xmin' : -101, 'xmax' : -94,
          'ymin' : 33.5, 'ymax' : 37.1,
          'projection' : 'merc', #or 'aea' for equal area projections
        }


#---------------------LOAD DATA--------------------------------
os.chdir(data_dir)

#load seismicity and welldata using loadtxt
mSeis = np.loadtxt(file_eq).T
mWells = np.loadtxt(file_well).T

#TODO: convert date-time to decimal year use seis_utils.dateTime2decYr
aTime = seis_utils.dateTime2decYr(mSeis[1],mSeis[2],mSeis[3],mSeis[4],mSeis[5],mSeis[6])
mSeis = np.array( [aTime, mSeis[7], mSeis[8], mSeis[-1]])


#---------------------EQ Rates, Cumulative #-------------------

#plot rate and cumulative number of events
if dPar['showRate'] == True:
    plt.figure(1)
    ax = plt.subplot(211)
    
    #compute seismocity rates using seis_utils.eqRate
    seisRate = seis_utils.eqRate(aTime, dPar['k'])
    totalEQ = np.cumsum(np.ones(len(aTime)))
    
    #TODO: plot seismocity rates
    ax.hist(aTime, dPar['k'])
    ax.set_ylabel('Earthquake Rate [ev/mo]')
    ax2 = plt.subplot(212)
    
    #TODO: plot cumulative number of earthquakes
    ax2.hist(aTime, totalEQ)
    ax2.set_xlabel('Time [dec. yr]')
    ax2.set_ylabel('Cumulative Number')
    ax2.set_xlim(ax.get_xlim())
    plt.show()
    
    
#---------------------MAP VIEW---------------------------------
#create time vector with dt_map spacing
at_bin = np.arange(dPar['tmin'], 2018, dPar['dt_map'])

for i in range(at_bin.shape[0]-1):
    t1, t2 = at_bin[i], at_bin[i+1]
    
    #TODO: Select earthquakes between t1 and t2 use 
    #np.logical_and sel_eq = np.logical_and(mSeis[0] >= t1, mSeis[0] < t2)
    sel_eq = np.logical_and(mSeis[0] >= t1, mSeis[0] < t2)
    
    #TODO: Select wells with start dates before t1
    sel_we = mWells[1] < t1
    
    print(t1, t2, 'No. earthquakes', sel_eq.sum(), 'No. of wells', sel_we.sum())
    
    #create basemap object
    plt.figure(2)
    plt.cla()
    ax2 = plt.subplot(111)
    lon_0, lat_0 = .5*(dPar['xmin'] + dPar['xmax']), .5*(
            dPar['ymin'] + dPar['ymax'])
    m = Basemap(llcrnrlon=dPar['xmin'], urcrnrlon=dPar['xmax'],
                llcrnrlat=dPar['ymin'], urcrnrlat=dPar['ymax'],
                lon_0 = lon_0, lat_0 = lat_0,
                resolution = 'l',
                projection=dPar['projection'], )
    
    #TODO: Draw state boundaries
    m.drawstates(linewidth=.5)
    
    #TODO: convert spherical to 2D coordinate system using basemap
    #x,y = m(sel_we[2],sel_we[3])
    x,y = m(mSeis[1][sel_eq], mSeis[2][sel_eq])
    x_w,y_w = m(mWells[2][sel_we], mWells[3][sel_we])
    
    #TODO: plot seismocity and well locations
    seisPlot = plt.scatter(x, y, c=mSeis[3][sel_eq], s=np.exp(mSeis[3][sel_eq]))
    wellPlot = plt.scatter(x_w,y_w, marker='^', alpha=0.09)
    
    #x and y labels
    m.drawparallels( np.arange( 33,   38,  1), fmt='%i',labels=[1,0,0,0])
    m.drawmeridians( np.arange(-100,  -92, 2), fmt='%i',labels=[0,0,0,1])
    
    if i == 0:
        c = plt.colorbar(seisPlot, orientation = 'horizontal')
        c.set_label('Magnitude')
    
    plt.pause(.5)
    
"""
Answer for part 1(e):
    
Based on this analysis it seems that earthquakes started occurring at a much
higher rate during the year 2010. The rate falls again after 2015, perhaps
because legislation required wells to be less active.
"""
