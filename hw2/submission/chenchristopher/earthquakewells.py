# -*- coding: utf-8 -*-
#python 2.7
"""
Creates plots to analyze the relationship between drilling wells in Oklahoma and the seismic
activity. Also creates a timelapse geographic map of wells and seismic activity for 6 month windows. 
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import decimal_years
from mpl_toolkits.basemap import Basemap
import area_polygon

#=========================================================================================
#load data
#=========================================================================================
os.chdir('./')
inj_data = np.loadtxt('injWell_OK.txt', comments = '#').T
seism_data = np.loadtxt('seism_OK.txt', comments = '#').T
                        
#must convert seism_data to decimal years
#seism_data1, 2, 3, 4, 5, 6 correspond to yrs, mos, dys, hrs, mins, secs respectively
decYear = decimal_years.dec_year(seism_data[1], seism_data[2], seism_data[3], seism_data[4],
                                 seism_data[5], seism_data[6])
#=========================================================================================
#parameters
#=========================================================================================
dPar  =  {   'dt_map'    : 0.5, # time step for plotting eq and wells in map view

             # for rate computations
             'k'         : 200,

             'tmin'      : 2005, # play with this number to visualize historic rates
             'tmax'      : 2018,
             # -----basemap params----------------------
             'xmin' : -101, 'xmax' : -94,
             'ymin' :   33.5, 'ymax' :  37.1,
             'projection' : 'merc',# or 'aea' for equal area projections
           }

#=========================================================================================
#computations
#=========================================================================================
def comp_rate( at, k_win):
    # smoothed rate from overlapping sample windows normalized by delta_t
    """
    Input: at is the time array of data
           k_win is the sampling window, eg. put 100 if you want to sample every 100
           independent variables
    Output: aBin is the array of average years of every sampling window k_win
            aRate is the array of average rates of change between sampling windows
    """
            
    aS          = np.arange( 0, at.shape[0]-k_win, 1)
    aBin, aRate = np.zeros(aS.shape[0]), np.zeros(aS.shape[0])
    iS = 0
    for s in aS:
        i1, i2 = s, s+k_win
        aBin[iS]  = 0.5*( at[i1]+at[i2])
        aRate[iS] = k_win/( at[i2]-at[i1])
        iS += 1
    return aBin, aRate

aBin, aRate = comp_rate(decYear, dPar['k'])

#==========================================================================================
#plotting
#==========================================================================================
plt.figure(1, figsize = (12, 10))
seisplot = plt.subplot(211)
seisplot.plot(aBin, aRate)
seisplot.set_xlabel('Average Year')
seisplot.set_ylabel('Average Annual Earthquake Rate')
print("Figure 1 Top: Every 200 data points were sampled and the average year and average earthquake rate between each sampling window were graphed.")
print("Figure 1 Bottom: Time vs. Cumulative Earthquakes")

cumeq = plt.subplot(212)
cumeq.plot(decYear, np.cumsum(np.ones(decYear.size)))
cumeq.set_xlabel('Year')
cumeq.set_ylabel('Cumulative Earthquakes')

#==========================================================================================
#mapping
#==========================================================================================
# create time vector with dt_map spacing
at_bin  = np.arange(dPar['tmin'], dPar['tmax'], dPar['dt_map'])
for i in range( at_bin.shape[0]-1):
    t1, t2 = at_bin[i], at_bin[i+1]
    #TODO: select earthquakes between t1 and t2 use np.logical_and
    sel_eq = np.logical_and(decYear  >= t1, decYear < t2)
    #TODO: select wells with start dates before t1
    sel_we = inj_data[1] < t1
    print(t1, t2, 'No. earthquakes', sel_eq.sum(), 'No. of wells', sel_we.sum())
    ### create basemap object
    plt.figure(2, figsize = (12, 10))
    plt.cla()
    #ax2 = plt.subplot(111)
    lon_0, lat_0 = .5*( dPar['xmin']+dPar['xmax']), .5*( dPar['ymin']+dPar['ymax'])
    m = Basemap(llcrnrlon = dPar['xmin'], urcrnrlon=dPar['xmax'],
                llcrnrlat = dPar['ymin'], urcrnrlat=dPar['ymax'],
                lon_0 = lon_0, lat_0 = lat_0,
                resolution = 'l',
                projection=dPar['projection'], )
    #TODO: draw state boundaries
    m.drawstates()

    #TODO: convert spherical to 2D coordinate system using basemap
    xeq, yeq = m(seism_data[7][sel_eq], seism_data[8][sel_eq])
    xwe, ywe = m(inj_data[2][sel_we], inj_data[3][sel_we])
    
    #storing the coordinates of year 2014, the first spike in seismic activity, to be used for finding the area of
    #the affected region
    if t1 == 2014.0:
        xeq2 = xeq
        yeq2 = yeq
        xwe2 = xwe
        ywe2 = ywe

    # TODO: plot seismicity and well locations
    eqmap = plt.scatter(xeq, yeq, c = 'red')
    wemap = plt.scatter(xwe, ywe, c = 'black')

    # x and y labels
    m.drawparallels( np.arange( 33,   38,  1), fmt='%i',labels=[1,0,0,0])
    m.drawmeridians( np.arange(-100,  -92, 2), fmt='%i',labels=[0,0,0,1])
    #--------------

    #file_out = 'OK_seis_t_%.1f_%.1f.png'%( t1, t2)
    #plt.savefig(  file_out, dpi = 150)
    #plt.clf()
   
    plt.pause( .5)

#===========================================================================================
#analysis
#===========================================================================================
print("Figure 2: Black represents wells up to current window and red represents earthquakes in the 6 month window.")
print("From figure 1, we see that seismicity rates start to increase dramatically higher than historic levels starting 2014. Earthquake rates started decreasing again in 2015. From figure 2, we can reason this decrease might be because the number of wells stopped increasing, it was the same starting 2015.")

#===========================================================================================
#computing area
#===========================================================================================
plt.figure(3, figsize = (12, 10))
plt.cla()
m = Basemap(llcrnrlon = dPar['xmin'], urcrnrlon=dPar['xmax'],
            llcrnrlat = dPar['ymin'], urcrnrlat=dPar['ymax'],
            lon_0 = lon_0, lat_0 = lat_0,
            resolution = 'l',
            projection=dPar['projection'], )
m.drawstates()
eq2map = plt.scatter(xeq2, yeq2, c = 'red')
we2map = plt.scatter(xwe2, ywe2, c = 'black')

#user input
print("Figure 3: Click on points to make a boundary. Middle click when finished inputting.")
tCoord = plt.ginput(n = -1, show_clicks = True)
x = np.array(tCoord).T[0]
y = np.array(tCoord).T[1]

#convert to equal area projection
#convert to longitude and lattitude first
lon, lat = m(x, y, inverse = True)

#now convert to 2D coordinates under the new projection
m = Basemap(llcrnrlon = dPar['xmin'], urcrnrlon=dPar['xmax'],
            llcrnrlat = dPar['ymin'], urcrnrlat=dPar['ymax'],
            lon_0 = lon_0, lat_0 = lat_0,
            resolution = 'l',
            projection = 'aea', )

xconv, yconv = m(lon, lat)

#compute area
xconv /= 1000 #convert to km
yconv /= 1000 #convert to km
area = area_polygon.area(xconv, yconv)
print("The area is " + str(area) + " square km. That's " + str(area / 180000) + " the size of Oklahoma!")
