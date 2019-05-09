# -*- coding: utf-8 -*-
"""
Homework 2
@author: collin O'Connor
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
#==============================================================================
#Question 1
#==============================================================================
#==============================================================================
#Part a
#==============================================================================
file_inj='injWell_OK.txt'
file_seism='seism_OK.txt'
mWell=np.loadtxt(file_inj).T
mSeis=np.loadtxt(file_seism).T

#==============================================================================
#Part b
#==============================================================================
def DecYear( YR, MO, DY, HR, MN, SC):
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

YR=np.genfromtxt(file_seism, skip_header=1, usecols=(1), dtype=float).T
MO=np.genfromtxt(file_seism, skip_header=1, usecols=(2), dtype=float).T
DY=np.genfromtxt(file_seism, skip_header=1, usecols=(3), dtype=float).T
HR=np.genfromtxt(file_seism, skip_header=1, usecols=(4), dtype=float).T
MN=np.genfromtxt(file_seism, skip_header=1, usecols=(5), dtype=float).T
SC=np.genfromtxt(file_seism, skip_header=1, usecols=(6), dtype=float).T

print('Decimal years:', DecYear(YR, MO, DY, HR, MN, SC))

#==============================================================================
#Part c
#==============================================================================
#earthquake rate will be in seconds
aT=DecYear(YR, MO, DY, HR, MN, SC)
k=200
def comp_rate(at, k_win):
    # smoothed rate from overlapping sample windows normalized by delta_t
    aS          = np.arange( 0, at.shape[0]-k_win,1)
    aBin = np.zeros(aS.shape[0])
    aRate = np.zeros(aS.shape[0])
    iS = 0
    for s in aS:
        i1, i2 = s, s+k_win
        aBin[iS]  = 0.5*( at[i1]+at[i2])
        aRate[iS] = k_win/( at[i2]-at[i1])
        iS += 1
    return aBin, aRate
print('seismicity rates:', comp_rate(aT,k))
aBin, aRate= comp_rate(aT, k)

with open(file_seism) as f:
    N=(sum(1 for _ in f)-1) #minus 1 because of the header
eqTotal=np.cumsum(np.ones(N))


plt.figure(1)
ax1 = plt.subplot( 211)
ax1.plot(aBin, aRate, 'b-')
ax1.set_ylabel( 'Earthquake Rate [ev/mo]')
ax1.set_xlabel( 'Time')

ax2 = plt.subplot( 212)
ax2.plot(aT, eqTotal, 'ko', ms=2.5)
ax2.set_xlabel( 'Time [dec. yr]')
ax2.set_ylabel('Cumulative Number')
ax2.set_xlim( ax1.get_xlim())
plt.show()
#==============================================================================
#d
#==============================================================================

dPar  =  {  'showRate'  : True,
            'dt_map'    : 6./12, # time step for plotting eq and wells in map view

             # for rate computations
             'k'         : 200,

             'tmin'      : 2015, # play with this number to visualize historic rates
             # -----basemap params----------------------
             'xmin' : -101, 'xmax' : -94,
             'ymin' :   33.5, 'ymax' :  37.1,
             'projection' : 'merc',# or 'aea' for equal area projections
           }

# create time vector with dt_map spacing
mSeis  = np.array( [aT, mSeis[7], mSeis[8], mSeis[-1]])
mWell= np.array([mWell[1], mWell[2], mWell[3], mWell[-1]])
at_bin  = np.arange( dPar['tmin'], 2018, dPar['dt_map'])

nWell=np.loadtxt(file_inj).T
nSeis=np.loadtxt(file_seism).T

mLoc = np.genfromtxt( file_seism, skip_header = 1, usecols=(7,8,10), dtype = float).T
# sort according to year of occurrence
sort_id = aT.argsort()
aYr = aT[sort_id]
mLoc= mLoc.T[sort_id].T


for i in range( at_bin.shape[0]-1):
    t1, t2 = at_bin[i], at_bin[i+1]
    #TODO: select earthquakes between t1 and t2 use np.logical_and
    sel_eq = np.logical_and( mSeis[0]  >= t1, mSeis[0]   < t2)
    #TODO: select wells with start dates before t1
    sel_we= (mWell[0]<t1 )
    print t1, t2, 'No. earthquakes', sel_eq.sum(), 'No. of wells', sel_we.sum()
    print 
    ### create basemap object
    plt.figure(2)
    plt.cla()
    ax3 = plt.subplot(111)
    lon_0, lat_0 = .5*( dPar['xmin']+dPar['xmax']), .5*( dPar['ymin']+dPar['ymax'])
    m = Basemap(llcrnrlon = dPar['xmin'], urcrnrlon=dPar['xmax'],
                llcrnrlat = dPar['ymin'], urcrnrlat=dPar['ymax'],
                lon_0 = lon_0, lat_0 = lat_0,
                resolution = 'l',
                projection=dPar['projection'] )
    #TODO: draw state boundaries
    m.fillcontinents(color='yellow')
    m.drawstates(linewidth=0.5, linestyle='solid', color='k')

    #TODO: convert spherical to 2D coordinate system using basemap

    aX_eq, aY_eq=m(nSeis[7][sel_eq], nSeis[8][sel_eq])
    aX, aY=m(nWell[2][sel_we], nWell[3][sel_we])

    # TODO: plot seismicity and well locations
    
    plt.plot(aX_eq, aY_eq, 'ro', ms=5, mew=1.5, mfc='none', label='seismicity')
    
    plt.plot(aX, aY, 'bo', ms=2, mew=1.5, mfc='none', label='Wells')
    plt.legend(loc='lower left')
  

    # x and y labels
    m.drawparallels( np.arange( 33,   38,  1), fmt='%i',labels=[1,0,0,0])
    m.drawmeridians( np.arange(-100,  -92, 2), fmt='%i',labels=[0,0,0,1])

    plt.pause( .5)


#==============================================================================
#e
#==============================================================================


print "From what I can see here in the plots, the the seismicity rates started to significantly"
print "exceed previous rates roughtly around the 2010 mark, and reached a peak value at 2015. After"
print "this point in time in 2015, the number of earthquakes started to decrease exponentially."
print "We can see that the cause for this is due to the fact that once Oklahoma stopped "
print "producing wells in 2014, the number of earthquakes started to drastically decrease as" 
print "time progressed."


#==============================================================================
#Question 2
#==============================================================================
#==============================================================================
#part a
#==============================================================================
sel    =mSeis[0]>dPar['tmin']
mSeis=mSeis.T[sel].T

mWells = np.loadtxt( file_inj).T


plt.figure(3)
ax4 = plt.subplot(111)
#:TODO plot wells

dPar  =  {  'showRate'  : True,
            'dt_map'    : 6./12, # time step for plotting eq and wells in map view

             # for rate computations
             'k'         : 200,

             'tmin'      : 2016, # play with this number to visualize historic rates
             # -----basemap params----------------------
             'nClicks' : 10,
             'xmin' : -101, 'xmax' : -94,
             'ymin' :   33.5, 'ymax' :  37.1,
             'projection' : 'merc',# or 'aea' for equal area projections
           }

ax_well, ay_well=mWells[2], mWells[3]
plt.scatter(ax_well, ay_well, c='b', s=1.0)
#:TODO plot seismicity
ax_eq, ay_eq=mSeis[1], mSeis[2]
plt.scatter(ax_eq, ay_eq, c='r')
print("Please click %i times"%( dPar['nClicks']))
tCoord = plt.ginput( dPar['nClicks'])
print("clicked", tCoord)
plt.show()

aLon =  np.array( tCoord).T[0]
aLat =  np.array( tCoord).T[1]


#==============================================================================
#part b
#==============================================================================
# project into equal area coordinate system
lon_0, lat_0 = .5*( dPar['xmin']+dPar['xmax']), .5*( dPar['ymin']+dPar['ymax'])
m = Basemap(llcrnrlon = dPar['xmin'], urcrnrlon=dPar['xmax'],
            llcrnrlat = dPar['ymin'], urcrnrlat=dPar['ymax'],
            projection=dPar['projection'], lon_0 = lon_0, lat_0 = lat_0)
#TODO: project into equal area coordinate system
aX, aY= m(aLon, aLat)
plt.plot(aX, aY)

#==============================================================================
#part c
#==============================================================================
#TODO: compute area using eis_utils.area_poly
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
A_seis = area_poly(aX, aY)
print 'total area affected by seismicity: ', A_seis
print 'fraction of area of OK', A_seis/(dPar['areaOK']) # about 1/3