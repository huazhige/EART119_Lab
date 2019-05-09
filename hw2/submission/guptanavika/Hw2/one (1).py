#!/bin/python2.7
"""

--> 1) load ANSS seismicity data and well locations for Oklahoma
--> 2) plot eq rates
--> 3) plot cumulative rate
--> 4) seismicity and well map in moving time windows



"""
from __future__ import division
import os
import matplotlib.pyplot as plt
#from matplotlib
import numpy as np

from mpl_toolkits.basemap import Basemap

#------------my modules-----------------------
#import seis_utils

#===================================================================================
#                         rate computation
#===================================================================================
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

#===================================================================================
#                         time and distance
#===================================================================================
def haversine( lon1, lat1, lon2, lat2, **kwargs):
    """
    haversine formula implementation
    https://en.wikipedia.org/wiki/Great-circle_distance
    great circle distance between two points
    :input   lon1, lat1
             lon2, lat2

    		  gR - Earth radius (global variable)
    :output  distance - great circle distance in meter
    """
    gR = 6378.137 # ~6370
    # convert to radians
    lon1 = lon1 * np.pi / 180
    lon2 = lon2 * np.pi / 180
    lat1 = lat1 * np.pi / 180
    lat2 = lat2 * np.pi / 180
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))
    distance = gR * c
    return distance

def dateTime2decYr( YR, MO, DY, HR, MN, SC):
    """
    - convert date time to decimal year
    :param YR: - int or arrays
    :param MO:
    :param DY:
    :param HR:
    :param MN:
    :param SC:
    :return:
    """
    nDays = 365.25
    return YR + (MO-1)/12 + (DY-1)/nDays  + HR/(nDays*24) + MN/(nDays*24*60) + SC/(nDays*24*3600)

def area_poly( aX, aY):
    """
    use:

    A = 0.1*abs( (x1*y2 + x2*y3 + xn-1*yn + xn*y1) - (y1*x2 + y2*x3 + ... + yn-1*xn + yn*x1))
    :param aX: - x-coordinates of all vertices
    :param aY: - y-coordinates of all vertices
    :return: A - area of polygon
    """
    #sumVert1 = (aX[0:-1]*aY[1::]).sum()+aX[-1]*aY[0]
    # or:
    sumVert1  = np.dot( aX[0:-1], aY[1::])+aX[-1]*aY[0]
    #sumVert2 = (aY[0:-1]*aX[1::]).sum()+aY[-1]*aX[0]
    # or:
    sumVert2  = np.dot(aY[0:-1], aX[1::])+aY[-1]*aX[0]
    #sum = (aX[0:-1]*aY[1::] - aY[0:-1]*aX[1::]).sum() + (aX[-1]*aY[0]-aY[-1]*aX[0])
    return 0.5*abs( sumVert1 - sumVert2)
#--------------------------0---------------------------------------------
#                     params, dirs, files
#------------------------------------------------------------------------
#data_dir   = ???
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

#--------------------------1---------------------------------------------
#                        load data
#------------------------------------------------------------------------
#os.chdir( data_dir)
# load seismicity and well data using loadtxt
mSeis  = np.loadtxt( file_eq).T




yr=mSeis[1]
mon=mSeis[2]
dy=mSeis[3]
hr=mSeis[4]
mn=mSeis[5]
sec=mSeis[6]

lon=mSeis[7]
lat=mSeis[8]
#print yr[1]

aTime = np.empty(len(yr))

for i in range(len(yr)-1):
	aTime[i]=dateTime2decYr( yr[i], mon[i], dy[i], hr[i], mn[i], sec[i])

#print aTime

mSeis  = np.array( [aTime, mSeis[7], mSeis[8], mSeis[-1]])
mWells = np.loadtxt( file_well).T

#--------------------------2---------------------------------------------
#                  earthquake rates, cumulative number
#------------------------------------------------------------------------

# plot rate and cumulative number of events
if dPar['showRate'] == True:
    plt.figure(1)
    ax = plt.subplot( 211)
    # compute seismicity rates using seis_utils.eqRate
    #for i in range(len(aTime))
    #	if (aTime[i]>2005)


    aBin, aRate = eqRate( aTime, 200)

    r=np.linspace(2009,2018,len(aRate))



    #print aBin

    #print aRate

    ax.plot( r, aRate, 'b-')

#ax.plot( aRate, aTime, 'b-')


    #ax.np.histogram( aRate, aBin, aRate)

ax.set_ylabel( 'Earthquake Rate [ev/mo]')






ax2 = plt.subplot( 212)



    #np.cumsum( np.ones( N)))
timeH=1974
cuml=0
counter=0

inter=(len(aTime))

x=np.zeros(40)
y=np.zeros(int((len(aTime))/4))

for j in range (731):
    
    if (aTime[j]<=timeH):
        
      cuml=cuml+1
    else:
      x[counter]=cuml
      y[counter]=timeH

      timeH=timeH+1
      counter=counter+1
        #print 'here'



for k in range (len(x)):
   # print y[k]
    print(x[k])
    #print aTime[k]
    
z=np.linspace(1974,2018,len(x))

ax2.plot( z, x, 'g-')


#plt.show()




ax2.set_xlabel( 'Time [dec. yr]')
ax2.set_ylabel('Cumulative Number')
#ax2.set_xlim( ax.get_xlim())
   
plt.show()


#--------------------------3---------------------------------------------
#                       map view of well and event locations
#------------------------------------------------------------------------
# create time vector with dt_map spacing
at_bin  = np.arange( dPar['tmin'], 2018, dPar['dt_map'])
u=0
for i in range( at_bin.shape[0]-1):
    t1, t2 = at_bin[i], at_bin[i+1]
    #TODO: select earthquakes between t1 and t2 use np.logical_and
    sel_eq = np.logical_and( mSeis[0]  >= t1, mSeis[0]   < t2)
    #TODO: select wells with start dates before t1
    sel_we=np.logical_and(mSeis[0]  < t1, mSeis[0]  > 0)
    print(t1, t2, 'No. earthquakes', sel_eq.sum(), 'No. of wells', sel_we.sum())
    ### create basemap object
    plt.figure(2)
    plt.cla()
    ax2 = plt.subplot(111)
    lon_0, lat_0 = .5*( dPar['xmin']+dPar['xmax']), .5*( dPar['ymin']+dPar['ymax'])
    m = Basemap(llcrnrlon = dPar['xmin'], urcrnrlon=dPar['xmax'],
                llcrnrlat = dPar['ymin'], urcrnrlat=dPar['ymax'],
                lon_0 = lon_0, lat_0 = lat_0,
                resolution = 'l',
                projection=dPar['projection'], )
    #TODO: draw state boundaries
    m.drawstates() 
    
    #haversine(lon_0, lat_0)
    
    #print mSeis[1]
   
    
   
    
    #x,y = m(mSeis[7], mSeis[8])
    
   # print mSeis[]
   
   
   
    lon=mSeis[1]
    lat=mSeis[2]
    
    #for u in range(len(lon)):
    x,y = m(lon, lat)
    m.plot(x, y, 'r.')
         #u=u+1
        
    
   
    
   
    #ax2.plot(lon, lat)  
   
    
    
    
      # x and y labels
    m.drawparallels( np.arange( 33,   38,  1), fmt='%i',labels=[1,0,0,0])
    m.drawmeridians( np.arange(-100,  -92, 2), fmt='%i',labels=[0,0,0,1])
    #--------------
   
