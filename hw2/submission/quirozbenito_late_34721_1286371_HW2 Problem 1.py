# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 19:30:19 2019
HW 2 Problem 1
@author: Benny Quiroz
"""
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np


"""
I can't make modules. I tried. So I'm just copying the relevant methods. 
"""

def dateTime2decYr( YR, MO, DY, HR, MN, SC):
    nDays = 365.25
    return YR + (MO-1)/12 + (DY-1)/nDays  + HR/(nDays*24) + MN/(nDays*24*60) + SC/(nDays*24*3600)

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


file_eq    = 'seism_OK.txt'
file_well  = 'injWell_OK.txt'

mSeis  = np.loadtxt( file_eq).T
#Converting to DecYear
aTime = dateTime2decYr( mSeis[1], mSeis[2], mSeis[3], mSeis[4], mSeis[5], mSeis[6])
mSeis  = np.array( [aTime, mSeis[7], mSeis[8], mSeis[-1]])
#Creating wells array with only times and locations
mWells = np.loadtxt( file_well).T
mWells = np.array([mWells[1], mWells[2], mWells[3]])

#Calculating eq rates and the points that we will plot them against using the 
#eqRate() function.
eqbins, eqrates = eqRate(aTime, dPar['k'])

#Making an array of cumulative number of earthquakes which is just an array asending
#by one up to the total. Plotting against time however will give a cumulative plot. 
cumquakes = np.cumsum(np.ones(len(aTime)))

#Making the first figure.
plt.figure(1)

#First subplot will be the eartquake rates over time. 
ax1 = plt.subplot(2,1,1)
ax1.plot(eqbins, eqrates)
ax1.set_xlabel('Time')
ax1.set_ylabel( 'Earthquake Rate [ev/mo]')

#Second plot will be the cumulative earthquakes over time. 
ax2 = plt.subplot(2,1,2)
ax2.plot(aTime, cumquakes)
ax2.set_xlabel('Time')
ax2.set_ylabel('Cumulative Number of Eqs')

plt.show()

"""
By looking at the plot, I would say that the earthquake rates increase greatly
at around 2014.
"""

#at_bin is just start times for each bin starting at 2005 and going up by
#six months or 0.5.
at_bin  = np.arange( dPar['tmin'], 2018, dPar['dt_map'])
for i in range( at_bin.shape[0]-1):
    #t1, t2 are the begining and end times for each bin
    t1, t2 = at_bin[i], at_bin[i+1]
    #Boolean array that is used to get eq times within curent bin. 
    sel_eq = np.logical_and(mSeis[0] >= t1, mSeis[0] < t2)
    #Makes an array that only contains those earthquake times and locations.
    quakes = [mSeis[0][sel_eq], mSeis[1][sel_eq], mSeis[2][sel_eq]]
    
    #Boolean array that is used to pick injections in bins six months  before the eq bins.
    sel_well = np.logical_and(mWells[0] >= t1 - .5, mWells[0] < t1)
    wells = [mWells[0][sel_well], mWells[1][sel_well], mWells[2][sel_well]]

    plt.figure(2)
    ax2 = plt.subplot(111)
    #Makes Oklahoma
    lon_0, lat_0 = .5*( dPar['xmin']+dPar['xmax']), .5*( dPar['ymin']+dPar['ymax'])
    m = Basemap(llcrnrlon = dPar['xmin'], urcrnrlon=dPar['xmax'],
                llcrnrlat = dPar['ymin'], urcrnrlat=dPar['ymax'],
                lon_0 = lon_0, lat_0 = lat_0, resolution = 'l',
                projection=dPar['projection'], )
    m.drawstates()
    #Converts to meters.
    qlon, qlat = m(quakes[1], quakes[2])
    wlon, wlat = m(wells[1], wells[2])
    #Plots earthquakes as blue dots and injections as red dots. 
    m.plot(qlon, qlat, 'bo', ms = 1)
    m.plot(wlon, wlat, 'ro', ms = 1)
    
    m.drawparallels( np.arange( 33,   38,  1), fmt='%i',labels=[1,0,0,0])
    m.drawmeridians( np.arange(-100,  -92, 2), fmt='%i',labels=[0,0,0,1])

    file_out = 'OK_seis_t_%.1f_%.1f.png'%( t1, t2)
    plt.savefig(  file_out, dpi = 150)
    
    plt.pause(0.5)
    
    
"""
With this one you've just got to know what you're looking at as the red dots are 
injections that are occuring about six months before the earthquakes that you see. 
"""
    

    




