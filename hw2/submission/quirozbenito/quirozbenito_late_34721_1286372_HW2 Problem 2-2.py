# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 15:12:36 2019
HW2 Problem #2
@author: Benny Quiroz
"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.basemap import Basemap

"""
I can't make my own modules so I had to slap these in here. 

"""

def dateTime2decYr( YR, MO, DY, HR, MN, SC):
    nDays = 365.25
    return YR + (MO-1)/12 + (DY-1)/nDays  + HR/(nDays*24) + MN/(nDays*24*60) + SC/(nDays*24*3600)

def area_polygon_vec(xs, ys):
    A = np.dot(xs, np.roll(ys,1)) - np.dot(ys, np.roll(xs, 1))
    A = np.abs(A)
    A = 0.5*A
    return A        



dPar  =  {   'nClicks' : 10,
             'tmin'    : 2010,
             'areaOK'  : 181*1e3,#in km
             # -----basemap params----------------------
             'xmin' : -101, 'xmax' : -94,
             'ymin' :   33.5, 'ymax' :  37.1,
             'projection' : 'aea',# or 'cea' 'aea' for equal area projections
           }

eqinfo  = np.loadtxt( 'seism_OK.txt').T
injinfo = np.loadtxt('injWell_OK.txt' ).T

#Converts the times in eqinfor to DecYear
aTime = dateTime2decYr( eqinfo[1], eqinfo[2], eqinfo[3], eqinfo[4], eqinfo[5], eqinfo[6])

#Rewrites aTime to only those after 2014
bool_array = aTime > 2014
aTime = aTime[bool_array]
eqinfo = np.array([aTime, eqinfo[7], eqinfo[8]])
eqlong = eqinfo[1]
eqlat  = eqinfo[2]

#makes these only the longs and lats after 2014
eqlong = eqlong[bool_array]
eqlat = eqlat[bool_array]

#Makes Oklahoma
lon_0, lat_0 = .5*( dPar['xmin']+dPar['xmax']), .5*( dPar['ymin']+dPar['ymax'])
m = Basemap(llcrnrlon = dPar['xmin'], urcrnrlon=dPar['xmax'],
            llcrnrlat = dPar['ymin'], urcrnrlat=dPar['ymax'],
            projection=dPar['projection'], lon_0 = lon_0, lat_0 = lat_0)
m.drawstates()
#Converts to meters 
x, y = m(eqlong, eqlat)
#Plots earthquakes in blue.
m.plot(x, y, 'bo', markersize = 1)

#Using ginput() so that the veiwer can calculate areas at their discretion. 
print("Please click %i times"%( dPar['nClicks']))
tCoord = plt.ginput( dPar['nClicks'])
print("clicked", tCoord)
#Converting to kilmeters so that we can give area in square kilometers. 
aLon =  np.array( tCoord).T[0]/1000
aLat =  np.array( tCoord).T[1]/1000

print ("The area of the region is", area_polygon_vec(aLon, aLat), "square kilometers.")   

"""
I clicked around only the densest region and it was about 15 percent of the total area. 
This does leave out a lot of earthquakes however and a less dense estimate would 
be about 45 percent.
"""
