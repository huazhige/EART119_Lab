# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 19:22:27 2019

@author: Emily White
"""

from __future__ import division
import os
import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.basemap import Basemap

import seis_utils



data_dir = '../data'
file_eq = 'seism_OK.txt'
file_well = 'injWell_OK.txt'

dPar = {    'nClicks'   :   10,
            'tmin'      :   2010,
            'areaOK'    :   181*1e3, #in km
            'xmin'  :   -101,   'xmax'  :   -94,
            'ymin'  :   33.5,   'ymax'  :   37.1,
            'projection'    :   'aea'}

os.chdir(data_dir)

mSeis = np.loadtxt(file_eq).T
#data time to decimal years
def dateTime2decYr(YR, MO, DY, HR, MN, SC):
    nDays = 365.25
    return YR + (MO - 1)/12 + (DY - 1)/nDays + HR/(nDays*24) + MN/(nDays*24*60) + SC/(nDays*24*3600)
aTime = mSeis[0], mSeis[1]
mSeis = np.array([aTime, mSeis[7], mSeis[8], mSeis[-1]])
# select most recent seismic events
sel = max(mSeis)
mSeis = mSeis.T[sel].T
mWells = np.loadtxt(file_well).T



plt.figure(1)
ax1 = plt.subplot(111)
#plot wells
plt.plot([mWells])
plt.ylabel('Wells')
plt.show()
#plot seismicity
plt.plot([mSeis])
plt.xlabel('Seismicity')
plt.show()



print("Please click %i times"%(dPar['nClicks']))
tCoord = plt.ginput(dPar['nClicks'])
print("clicked", tCoord)
plt.show()


aLon = np.array(tCoord).T[0]
aLat = np.array(tCoord).T[1]

lon_0, lat_0 = (dPar['xmin']+dPar['xmax'])/2, (dPar['ymin']+dPar['ymax'])/2
m = Basemap(llcrnrlon = dPar['xmin'], urcrnrlon=dPar['xmax'],llcrnrlat = dPar['ymin'], 
            urcrnrlat=dPar['ymax'],projection=dPar['projection'], 
            lon_0 = lon_0, lat_0 = lat_0)

#project into equal area coordinate system
m.drawcoastlines()
m.drawcountries()
m.fillcontinents(color='brown', lake_color='blue')
m.drawparallels(np.arange(33, 38, 1))
m.drawmeridians(np.arange(-100,-92, 2))
m.drawmapboundary(fill_color='blue')

ax = plt.gca()
for y in np.linspace(m.ymax/2,19*m.ymax/2,10):
    for x in np.linspace(m.xmax/1,19*m.xmax/1,12):
        lon,lat = m(x,y,inverse=True)
        poly = m.tissot(lon,lat,2,100, facecolor = 'green', zorder= 5, alpha=0.5)
        
plt.show()

def eq_rate(at, k_win):
    aS      = np.arange(0,at.shape[0]-k_win, 1)
    aBin, aRate = np.zeros(aS.shape[0]), np.zeros(aS.shape[0])
    iS = 0
    for s in aS:
        i1, i2 = s, s+k_win
        aBin[iS] = (at[i1]+at[i2])/2
        aRate[iS] = k_win/(at[i2]-at[i1])
        iS += 1
    return aBin, aRate

A_seis = seis_utils.area_poly( mSeis, mWells)
print 'total area affected by seismicity: ', A_seis
print 'fraction of area of OK', A_seis/(dPar['areaOK']) # about 1/3







