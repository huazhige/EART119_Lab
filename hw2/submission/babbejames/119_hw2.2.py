#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: jtbabbe
"""


import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.basemap import Basemap

#------------my modules-----------------------
import seis_utils
#--------------------------0---------------------------------------------
#                     params, dirs, files, equations
#------------------------------------------------------------------------
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

def DecYear( YR, MO, DY, HR, MN, SC):
    return YR + (MO-1)/12 + (DY-1)/365.25 + HR/(365.25) + MN/(365.25*24*60)
    + SC/(365.25*24*3600)
    
#--------------------------1---------------------------------------------
#                        load data
#------------------------------------------------------------------------
# load seismicity and well data using loadtxt
mSeis  = np.loadtxt( file_eq).T
#time to decimal years
# Decimal year eq
YR = mSeis[1]
MO = mSeis[2]
DY = mSeis[3]
HR = mSeis[4]
MN = mSeis[5]
SC = mSeis[6]

aTime  = DecYear( YR, MO, DY, HR, MN, SC)
mSeis  = np.array( [aTime, mSeis[7], mSeis[8], mSeis[-1]])
#select most recent seismic events
sort_id = aTime.argsort()
sel    = aTime[sort_id]
mSeis  = mSeis.T[sel].T
mWells = np.loadtxt( file_well).T

#--------------------------2---------------------------------------------
#                       map view, select boundaries of seismicity
#------------------------------------------------------------------------

pat_bin  = np.arange( dPar['tmin'], 2018, dPar['dt_map'])
for i in range( at_bin.shape[0]-1):
    t1, t2 = at_bin[i], at_bin[i+1]
    #select earthquakes after 2010
    sel_eq =  mSeis[0]  >= 'tmin'
    #select wells with start dates after tmin
    sel_well = mWells[1] >= 'tmin'
    # create basemap object
    plt.figure(2)
    plt.cla()
    ax2 = plt.subplot(111)
    lon_0, lat_0 = .5*( dPar['xmin']+dPar['xmax']), .5*( dPar['ymin']+dPar['ymax'])
# project into equal area system
m = Basemap(llcrnrlon = dPar['xmin'], urcrnrlon=dPar['xmax'],
            llcrnrlat = dPar['ymin'], urcrnrlat=dPar['ymax'],
            projection=dPar['projection'], lon_0 = lon_0, lat_0 = lat_0)
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
print("Please click %i times"%( dPar['nClicks']))
tCoord = plt.ginput( dPar['nClicks'])
print("clicked", tCoord)
plt.show()

aLon =  np.array( tCoord).T[0]
aLat =  np.array( tCoord).T[1]


#--------------------------3---------------------------------------------
#               compute affected area
#------------------------------------------------------------------------
#TODO: compute area using eis_utils.area_poly
def area_poly( aX, aY):
    sumVert1  = np.dot( aX[0:-1], aY[1::])+aX[-1]*aY[0]
    sumVert2  = np.dot(aY[0:-1], aX[1::])+aY[-1]*aX[0]
    sum = (aX[0:-1]*aY[1::] - aY[0:-1]*aX[1::]).sum() + (aX[-1]*aY[0]-aY[-1]*aX[0])
    return 0.5*abs( sumVert1 - sumVert2)
A_seis = area_poly(aLon, aLat)
print('total area affected by seismicity: ', A_seis)
print( 'fraction of area of OK', A_seis/(dPar['areaOK'])) # about 1/3

