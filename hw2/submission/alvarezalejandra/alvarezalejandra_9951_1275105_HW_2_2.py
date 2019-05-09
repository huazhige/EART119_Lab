
from __future__ import division
import os
import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.basemap import Basemap

# my modules
import seis_utils
#data-time to decimal years
def decyear(YR, MO, DY, HR, MN, SC):
    decyear_final = YR + (MO-1)/12 + (DY-1)/365.25+ HR/(365.25*24) + MN/(365.25*24*60) + SC/(365.25*24*3600)
    return(decyear_final)
#--------------------------0---------------------------------------------
#                     params, dirs, files
#------------------------------------------------------------------------

file_eq    = 'seism_OK.txt'
file_well  = 'injWell_OK.txt'

dPar  =  {   'nClicks' : 10,
             'tmin'    : 2010,
             'areaOK'  : 181*1e3,#in km
             # basemap params
             'xmin' : -101, 'xmax' : -94,
             'ymin' :   33.5, 'ymax' :  37.1,
             'projection' : 'aea',# 'use aea' for equal area projections
           }

#--------------------------1---------------------------------------------
#                        load data
#------------------------------------------------------------------------

# load seismicity and well data using loadtxt
mSeis  = np.loadtxt( file_eq).T
#define data-time to decimal years
aTime  = decyear(YR, MO, DY, HR, MN, SC)
mSeis  = np.array( [aTime, mSeis[7], mSeis[8], mSeis[-1]])
mSeis  = mSeis.T
mWells = np.loadtxt( file_well).T

#--------------------------2---------------------------------------------
#                       map view, select boundaries of seismicity
#------------------------------------------------------------------------
plt.figure(1)
ax1 = plt.subplot(111)
#plot wells
x,y = map(aTime, mWells)
map.plot(x, y, 'bo', markersize=24)
#plot seismicity
x,y = map(aTime, mSeis)
map.plot(x, y, 'ro', markersize=24)
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



#--------------------------3---------------------------------------------
#               compute affected area
#------------------------------------------------------------------------
#compute area using eis_utils.area_poly
A_seis = 0.5*abs( sumVert1 - sumVert2)
def area_poly( aX, aY):
     sum = (aX[0:-1]*aY[1::] - aY[0:-1]*aX[1::]).sum() + (aX[-1]*aY[0]-aY[-1]*aX[0])
     sumVert1 = (aX[0:-1]*aY[1::]).sum()+aX[-1]*aY[0]
     sumVert2 = (aY[0:-1]*aX[1::]).sum()+aY[-1]*aX[0]
     return 0.5*abs( sumVert1 - sumVert2)
print('total area affected by seismicity: ', A_seis)
print('fraction of area of OK', A_seis/(dPar['areaOK'])) # about 1/3


#-----------------------------------------------------------------------
#  Compute the total area of the region affected by induced 
#   seismicity using the previously created function area_polygon.py. 
#   How does that compare to the total area of Oklahoma (181,000 km 2)?
#------------------------------------------------------------------------
#using the area found in part 3, to the total area of Oklahoma which is 
#  181,000 km^2

