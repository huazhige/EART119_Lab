# -*- coding: utf-8 -*-
"""
Spyder Editor

Hw2_problem 1
Earthquake rates, earthquake and well locations in map-view
author: JamesBabbe

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

#=====================================================
#           data set up
#=====================================================
# load files
file_inj         = './injWell_OK.txt'
file_seism       = './seism_OK.txt'

# transpose files
mWells           = np.loadtxt( file_inj).T
mSeis           = np.loadtxt( file_seism).T

# select window
k = 200
#=====================================================
#           function def
#=====================================================

# convert dataframe table into deciyears
def DecYear( YR, MO, DY, HR, MN, SC):
    return YR + (MO-1)/12 + (DY-1)/365.25 + HR/(365.25) + MN/(365.25*24*60)
    + SC/(365.25*24*3600)


# determine rate    
def comp_rate( a_t, k): 
    aS = np.arange( 0, a_t.shape[0]-k, 1)
    a_bin = np.zeros(aS.shape[0])
    a_rate = np.zeros( aS.shape[0])
    iS = 0
    for s in aS:
        i1, i2 = s, s+k
        a_bin[iS] = .5*( a_t[i1]+ a_t[i2])
        a_rate[iS] = k/( a_t[i2]-a_t[i1])
        iS += 1
    return a_bin, a_rate


#=====================================================
#           figure out Time and Rate
#=====================================================

# define variables for deciyear eq
YR = mSeis[1]
MO = mSeis[2]
DY = mSeis[3]
HR = mSeis[4]
MN = mSeis[5]
SC = mSeis[6]
decYear = (DecYear( YR, MO, DY, HR, MN, SC))
 
# convert deciyear to seconds
a_T = (decYear * 3.154e7)
print (a_T) 

print (comp_rate(a_T, k))

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

mSeis  = np.array( [a_T, mSeis[7], mSeis[8], mSeis[-1]])
#=====================================================
#           plot static graph
#=====================================================
#get cumulative sum
quake_sum = np.cumsum( np.ones( len(mSeis)))

mag = mData2[-1]
depth = mData2[-2]

plt.figure(2)
ax1 = plt.subplot( 211)
ax1.plot( decYear, a_rate)
ax2 = plt.subplot( 212)
ax2.plot( decYear, depth)

#=====================================================
#           plot updating graph
#=====================================================

at_bin  = np.arange( dPar['tmin'], 2018, dPar['dt_map'])
for i in range( at_bin.shape[0]-1):
    t1, t2 = at_bin[i], at_bin[i+1]
    #select earthquakes between t1 and t2 use np.logical_and
    sel_eq = np.logical_and( mSeis[0]  >= t1, mSeis[0]   < t2)
    #select wells with start dates before t1
    sel_well = mWells[1] >= t1
    # create basemap object
    plt.figure(2)
    plt.cla()
    ax2 = plt.subplot(111)
    lon_0, lat_0 = .5*( dPar['xmin']+dPar['xmax']), .5*( dPar['ymin']+dPar['ymax'])
    m = Basemap(llcrnrlon = dPar['xmin'], urcrnrlon=dPar['xmax'],
                llcrnrlat = dPar['ymin'], urcrnrlat=dPar['ymax'],
                lon_0 = lon_0, lat_0 = lat_0
                resolution = 'c'
                projection = dPar['projection'], )
#draw state boundaries
m.drawstates(color = 'aqua')

#convert spherical to 2D coordinate system using basemap
xpt_Seis, ypt_Seis = m(mSeis[-4][sel_eq], mSeis[-3][sel_eq])
xpt_Well, ypt_Well = m(mWell[3][sel_well],mWell[4][sel_well])

#plot seismicity and well locations
plt.plot(xpt_Seis, ypt_Seis, 'ro', ms = 6, mew = 1.5, mfc = 'none', label = 'seismicity')
plt.plot(xpt_Well, ypt_Well, 'bo', ms = 6, mew = 1.5, mfc = 'none', label = 'wells')

# x and y labels
m.drawparallels( np.arange( 33,   38,  1), fmt='%i',labels=[1,0,0,0])
m.drawmeridians( np.arange(-100,  -92, 2), fmt='%i',labels=[0,0,0,1])
    


    plt.pause( .5)







