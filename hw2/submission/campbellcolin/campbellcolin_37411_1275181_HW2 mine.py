from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.basemap import Basemap
import seis_utils

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

seism_OK_Data = np.loadtxt('seism_OK.txt').T
Wells_OK_Data = np.loadtxt('injWell_OK.txt').T

#--------------------------1---------------------------------------------
#                        load data
#------------------------------------------------------------------------

mSeis  = np.loadtxt( file_eq).T
aTime = seis_utils.dateTime2decYr(seism_OK_Data[1], seism_OK_Data[2], seism_OK_Data[3], seism_OK_Data[4], seism_OK_Data[5], seism_OK_Data[6] )
mSeis  = np.array( [aTime, mSeis[7], mSeis[8], mSeis[-1]])
mWells = np.loadtxt( file_well).T

#--------------------------2---------------------------------------------
#                  earthquake rates, cumulative number
#------------------------------------------------------------------------
if dPar['showRate'] == True:
    plt.figure(1, figsize = (12, 5))
    ax = plt.subplot( 211)
    # compute seismicity rates
    aBin, aRate = seis_utils.eqRate( aTime, 200 )
    plot1 = plt.plot(aBin, aRate)

    ax.set_ylabel( 'Earthquake Rate [ev/mo]')
    ax2 = plt.subplot( 212)
    plot2 = plt.plot(aTime, np.cumsum(np.ones(7200)))

    ax2.set_xlabel( 'Time [dec. yr]')
    ax2.set_ylabel('Cumulative Number')
    ax2.set_xlim( ax.get_xlim())
    plt.show()

#--------------------------3---------------------------------------------
#                       map view of well and event locations
#------------------------------------------------------------------------

at_bin  = np.arange( dPar['tmin'], 2018, dPar['dt_map'])
for i in range( at_bin.shape[0]-1):
    t1, t2 = at_bin[i], at_bin[i+1]
    sel_eq = np.logical_and( mSeis[0]  >= t1, mSeis[0]   < t2)
    sel_we = mWells[1] < t1
    print(t1, t2, 'No. earthquakes', sel_eq.sum(), 'No. of wells', sel_we.sum())
    ### create basemap object
    plt.figure(2, figsize = (20, 15))
    plt.cla()
    ax2 = plt.subplot(111)
    lon_0, lat_0 = .5*( dPar['xmin']+dPar['xmax']), .5*( dPar['ymin']+dPar['ymax'])
    m = Basemap(llcrnrlon = dPar['xmin'], urcrnrlon=dPar['xmax'],
                llcrnrlat = dPar['ymin'], urcrnrlat=dPar['ymax'],
                lon_0 = lon_0, lat_0 = lat_0,
                resolution = 'l',
                projection=dPar['projection'], )
    m.drawstates()

    #TODO: convert spherical to 2D coordinate system using basemap
    xearth, yearth = m(seism_OK_Data[7][sel_eq], seism_OK_Data[8][sel_eq])
    wellx, welly = m(Wells_OK_Data[2][sel_we], Wells_OK_Data [3][sel_we])

    # TODO: plot seismicity and well locations
    plot2 = plt.scatter(xearth, yearth, c = "red")
    plot3 = plt.scatter(wellx, welly, c = "black")

    # x and y labels
    m.drawparallels( np.arange( 33,   38,  1), fmt='%i',labels=[1,0,0,0])
    m.drawmeridians( np.arange(-100,  -92, 2), fmt='%i',labels=[0,0,0,1])
    #--------------

    #file_out = 'OK_seis_t_%.1f_%.1f.png'%( t1, t2)
    #plt.savefig(  file_out, dpi = 150)
    #plt.clf()
    if t1 == 2013.5:
        xearth = xearth
        yearth = yearth
        xwell = wellx
        ywell = welly
    plt.pause( .01)


#--------------------------4---------------------------------------------
#                       Problem 2
#------------------------------------------------------------------------

plt.figure(3, figsize = (20, 15))
plt.cla()
ax2 = plt.subplot(111)
lon_0, lat_0 = .5*( dPar['xmin']+dPar['xmax']), .5*( dPar['ymin']+dPar['ymax'])
m = Basemap(llcrnrlon = dPar['xmin'], urcrnrlon=dPar['xmax'],
                llcrnrlat = dPar['ymin'], urcrnrlat=dPar['ymax'],
                lon_0 = lon_0, lat_0 = lat_0,
                resolution = 'l',
                projection=dPar['projection'], )
m.drawstates()


plot4 = plt.scatter(xearth, yearth, c = "red")
plot5 = plt.scatter(xwell, ywell, c = "black")

tCoord = plt.ginput( n = -1, show_clicks = True)
X = np.array( tCoord).T[0]
Y = np.array( tCoord).T[1]

lon, lat = m(X, Y, inverse = True)

m = Basemap(llcrnrlon = dPar['xmin'], urcrnrlon=dPar['xmax'],
                llcrnrlat = dPar['ymin'], urcrnrlat=dPar['ymax'],
                lon_0 = lon_0, lat_0 = lat_0,
                resolution = 'l',
                projection = 'aea', )

xconv, yconv = m(lon, lat)

xconv /= 1000
yconv /= 1000

area = seis_utils.area_poly(xconv, yconv)
print("The area encompassed is " + str(area) + " square kilometers which is " + str(area/1800) + "% of the state!")
