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

#------------my modules-----------------------
import seis_utils
#--------------------------0---------------------------------------------
#                     params, dirs, files
#------------------------------------------------------------------------
data_dir   = '~/Users/Victor/Downloads/'
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

#--------------------------1---------------------------------------------
#                        load data
#------------------------------------------------------------------------
# load seismicity and well data using loadtxt
injWell_OK  = np.loadtxt( file_well)
seism_OK  = np.loadtxt( file_eq)
np.transpose(injWell_OK)
np.transpose(seism_OK)
seism_OK_decimals = []
seism_OK_ints = []
for a in seism_OK:
	d = a[1] + ((a[2]-1)/12) + ((a[3]-1)//365.25) + ((a[4]-1)/(365.25*24)) + ((a[5])/(365.25*24*60)) + ((a[6])/(365.25*24*3600)) 
	t = d.round()
	if t not in seism_OK_ints:
		seism_OK_ints.append(t)
	seism_OK_decimals.append(d)
# print(seism_OK_decimals)
plt.hist(seism_OK_decimals, bins=seism_OK_ints)
plt.ylabel('Quantity');
plt.show()
aYr  = np.genfromtxt( eqFile, skip_header = 1, usecols=(0), delimiter='-', dtype = int)
mLoc = np.genfromtxt( eqFile, skip_header = 1, usecols=(2,1), delimiter=',', dtype = float).T
mLoc = np.genfromtxt( eqFile, skip_header = 1, usecols=(2,1,4), delimiter=',', dtype = float).T

#:TODO data-time to decimal years
aTime  = getYear(aYr)
mSeis  = np.array( [aTime, mSeis[7], mSeis[8], mSeis[-1]])

#TODO: select most recent seismic events
sort_id = aYr.argsort()
sel    = aYr[sort_id]
mSeis  = mSeis.T[sel].T
mWells = np.loadtxt( file_well).T
for it in np.unique( aYr, xmin, xmax, ymin, ymax, projection):
    sel_eq = it == aYr
    print( 'current year', it, '#no. of events: ', sel_eq.sum())
    ### create basemap object
    plt.figure( 1)
    plt.cla()
    plt.title( str( it))
    lon_0, lat_0 = .5*( xmin + xmax), .5*( ymin + ymax)
    # Input kewords and plotting parameters in this function. llcrnlon is the minimum
    # value of the longitude, urcrnrlon is the maximum value of the longitude. Similarly,
    # you are going to input information about latitude later.
    m = Basemap(projection = 'cyl',
                llcrnrlon = xmin, urcrnrlon=xmax,
                llcrnrlat = ymin, urcrnrlat=ymax,
                 resolution = 'c', lon_0 = lon_0, lat_0 = lat_0)
    m.drawcoastlines()
    # get X axis and Y axis (longitude and latitude) of the dateset from the first and the
    # second column of the dataset.
    aX_eq, aY_eq = m(  mLoc[0][sel_eq], mLoc[1][sel_eq])

    #m.plot(  aX_eq, aY_eq, 'ro', ms = 6, mew = 1.5, mfc = 'none')
    # plot the scattered points of the dataset.
    plot1 =     plt.scatter( aX_eq, aY_eq, c = mLoc[2][sel_eq], s = np.exp( mLoc[2][sel_eq]-3))
    # plot colorbar in the horizontal direction
    cbar  = plt.colorbar( plot1, orientation = 'horizontal')
    cbar.set_label( 'Magnitude')
    #--------------
    #plt.savefig(  file_out, dpi = 150)
    #
    plt.pause( .5)
    #plt.show()
    plt.clf()

#--------------------------2---------------------------------------------
#                       map view, select boundaries of seismicity
#------------------------------------------------------------------------
plt.figure(1)
ax1 = plt.subplot(111)
#:TODO plot wells
plot2 =     plt.scatter( aX_eq, aY_eq, c = mLoc[2][sel_eq], s = np.exp( mLoc[2][sel_eq]-3))
#:TODO plot seismicity
plot3 =     plt.scatter( aX_eq, aY_eq, c = mLoc[2][sel_eq], s = np.exp( mLoc[2][sel_eq]-3))
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
A_seis = ???
print 'total area affected by seismicity: ', A_seis
print 'fraction of area of OK', A_seis/(dPar['areaOK']) # about 1/3

getYear(aYr){
	for x in aYr:
		for y in aYr[x]:
			DecYear = aYR[x,y]+ aYR[x-1,y+1]/12 + aYR[x-1,y+2]/12 + aYR[x-1,y+3]/(365.25*24) 
			+ aYR[x-1,y+4]/(365.25*24*60) + aYR[x-1,y+4]/(365.25*24*3600)
	
	return DecYear
}







