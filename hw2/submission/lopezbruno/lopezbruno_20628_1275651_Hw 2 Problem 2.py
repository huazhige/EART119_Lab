#!/bin/python2.7
"""

--> 1) load OK seismicity and well data
--> 2) plot eqs and wells using matplotlib
--> 3) select polygon that encompasses seism., project to equal area
       and compute area of polygon



"""
from __future__ import division
import os
import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.basemap import Basemap

#------------my modules-----------------------
import seis_utils
#--------------------------0---------------------------------------------
#                     params, dirs, files
#------------------------------------------------------------------------

os.chdir("./")
file_eq    = 'seism_OK.txt'
file_well  = 'injWell_OK.txt'

dPar  =  {   'nClicks' : 10,
             'tmin'    : 2010,
             'areaOK'  : 181*1e3,#in km
             # -----basemap params----------------------
             'xmin' : -101, 'xmax' : -94,
             'ymin' :   33.5, 'ymax' :  37.1,
             'projection' : 'aea',# or 'cea' 'aea' for equal area projections
           }


def areaForLoops(xi,yi):
    
    a = 0 # a placeholder, will contain (x0y1 + x1y2 + ... x(n-1)yn + xny1)
    b = 0  # a placeholder, will contain (y0x1 + y1x2 + ... y(n-1)xn + ynx1)
    i = 0 #Index counter for finding a
    j = 0 #Index counter for finding b
    
    #Finds the value of a using (x0y1 + x1y2 + ... x(n-1)yn + xny1)
    for i in range(0,len(xi) - 1):
        a += (xi[i] * yi[i+1])
        i += 1
    
    #This is to find the last term, the xny1 term
    a += xi[-1] * yi[0]
    
    #Finds the value of B using(y0x1 + y1x2 + ... y(n-1)xn + ynx1)
    for j in range(0,len(yi) - 1):
         b += (yi[j] * xi[j+1])
         j += 1
    
    #This is to find the last term, the ynx1 term    
    b += yi[-1] * xi[0]
         
     #returns the desired equation    
    return 0.5 * (a-b)

def decimalToYear(Year, Month, Day, Hour, minute, second):
    return Year + ((Month - 1)/12) + ((Day-1)/365.25) + (Hour/(365.25*24))  \
+ (minute /(365.25*24*60)) + (second/(365.25*24*3600))



#--------------------------1---------------------------------------------
#                        load data
#------------------------------------------------------------------------
mSeis  = np.loadtxt( file_eq).T

yr = mSeis[1] # Years
month = mSeis[2] #Months
day = mSeis[3] #Day
hour = mSeis[4] #Hour
minute = mSeis[5] #Minute
second = mSeis[6] #Second



mSeis1 = np.loadtxt(file_eq)
#:TODO data-time to decimal years
aTime  = decimalToYear(yr,month,day,hour,minute,second)
mSeis  = np.array( [aTime, mSeis[7], mSeis[8], mSeis[-1]])
#TODO: select most recent seismic events
sel    = mSeis1[717:7999]
mWells = np.loadtxt( file_well).T

#--------------------------2---------------------------------------------
#                       map view, select boundaries of seismicity
#------------------------------------------------------------------------
plt.figure(1)
ax1 = plt.subplot(111)
#:TODO plot wells
plt.plot(mSeis[0])
#:TODO plot seismicity

print("Please click %i times"%( dPar['nClicks']))
tCoord = plt.ginput( dPar['nClicks'])
print("clicked", tCoord)
plt.show()

aLon =  np.array( tCoord).T[0]
aLat =  np.array( tCoord).T[1]


# project into equal area coordinate system
lon_0, lat_0 = .5*( dPar['xmin']+dPar['xmax']), .5*( dPar['ymin']+dPar['ymax'])
m = Basemap(llcrnrlon = dPar['xmin'], urcrnrlon=dPar['xmax'],
            llcrnrlat = dPar['ymin'], urcrnrlat=dPar['ymax'],
            projection=dPar['projection'], lon_0 = lon_0, lat_0 = lat_0)
#TODO: project into equal area coordinate system



#--------------------------3---------------------------------------------
#               compute affected area
#------------------------------------------------------------------------
#TODO: compute area using eis_utils.area_poly
A_seis = areaForLoops(aLon,aLat)
print('total area affected by seismicity: ', A_seis)
print('fraction of area of OK', A_seis/(dPar['areaOK'])) # about 1/3







