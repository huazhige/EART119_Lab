# -*- coding: utf-8 -*-
"""
Seismic activity surface area
"""

from __future__ import division
import os
import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.basemap import Basemap

import seis_utils

#---------------------DATA DIRECTORY---------------------------
data_dir = './'
file_eq = 'seism_OK.txt'
file_well = 'injWell_OK.txt'

dPar = {    'nClicks' : 10,
            'tmin'    : 2010,
            'areaOK'  : 181*1e3, #in km
            'xmin'    : -101, 'xmax' : -94,
            'ymin'    : 33.5, 'ymax' : 37.1,
            'projection' : 'aea', #or 'cea' 'aea' for equal area projections
        }

#---------------------LOAD DATA--------------------------------
os.chdir(data_dir)

#load seismicity and well data using loadtxt
mSeis = np.loadtxt(file_eq).T
mWells = np.loadtxt(file_well).T

#TODO: data-time to decimal years
aTime = seis_utils.dateTime2decYr(mSeis[1],mSeis[2],mSeis[3],mSeis[4],mSeis[5],mSeis[6])
mSeis = np.array( [aTime, mSeis[7], mSeis[8], mSeis[-1]])

#TODO: select most recent seismic events
sel = mSeis[0] >= 2010
sel_we = mWells[1] > 2010
mSeis = mSeis.T[sel].T

#---------------------MAP VIEW---------------------------------
plt.figure(1)
ax1 = plt.subplot(111)

#project into equal area coordinate system
lon_0,lat_0 = .5*(dPar['xmin']+dPar['xmax']), .5*(dPar['ymin']+dPar['ymax'])
m = Basemap(llcrnrlon = dPar['xmin'], urcrnrlon=dPar['xmax'],
            llcrnrlat = dPar['ymin'], urcrnrlat=dPar['ymax'],
            projection=dPar['projection'], lon_0=lon_0, lat_0=lat_0)
m.drawstates(linewidth=.5)
m.drawparallels(np.arange(-80.,81.,20.,))
m.drawmeridians(np.arange(-180.,181.,20.))

#TODO: plot wells
x_w,y_w = m(mWells[2][sel_we], mWells[3][sel_we])
wellPlot = plt.scatter(x_w,y_w, marker='^', alpha=0.08)
#TODO: plot seismicity
x,y = m(mSeis[1], mSeis[2])
seisPlot = plt.scatter(x,y, c=mSeis[3], s=np.exp(mSeis[3]))

print("Please click %i times"%(dPar['nClicks']))
tCoord = plt.ginput(dPar['nClicks'])
print("clicked", tCoord)
plt.show()

aLon = np.array(tCoord).T[0]
aLat = np.array(tCoord).T[1]
area = [aLon[0::]/1e3,aLat[0::]/ 1e3] #conversion to kilometers


#TODO: project into equal area coordinate system

#I'm not sure how to use equal area coordinate systems
polyPlot = plt.scatter(aLon,aLat)
plt.show()
        
#---------------------COMPUTE AFFECTED AREA--------------------
#TODO: compute area using seis_utils.area_poly
A_seis = seis_utils.area_poly(area[0],area[1])
print('total area affected by seismicity: ', A_seis)
print('fraction of area of OK', A_seis/(dPar['areaOK'])) #about 1/3





