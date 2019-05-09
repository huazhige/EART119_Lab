

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap



#eqRate module (works better when I do not call from a separate folders)
def eqRate( at, k_win):
    # smoothed rate from overlapping sample windows normalized by delta_t
    aS          = np.arange( 0, at.shape[0] - k_win, 1)
    aBin, aRate = np.zeros(aS.shape[0]), np.zeros(aS.shape[0])
    iS = 0
    for s in aS:
        i1, i2 = s, s+k_win
        aBin[iS]  = 0.5*( at[i1]+at[i2])
        aRate[iS] = k_win/( at[i2]-at[i1])
        iS += 1
    return aBin, aRate


#=============================================================================
# 1.A
#=============================================================================
#                        Naming Files                 
#=============================================================================
file1 = 'injWell_OK.txt' #naming files for easier coding
file2 = 'seism_OK.txt'

#=============================================================================
#                        Load Data      
#=============================================================================
data1 = np.loadtxt( file1).T #imports files from computer
data2 = np.loadtxt( file2).T

#=============================================================================
# 1.B
#=============================================================================
#                       Load Columns Separately
#=============================================================================
YR  = data2[1,:]  #calling each column separately and labeling them
MO  = data2[2,:]
DY  = data2[3,:]
HR  = data2[4,:]
MN  = data2[5,:]
SC  = data2[6,:]

#=============================================================================
#                      convert date-time column to decimal years       
#=============================================================================
def decyear(YR, MO, DY, HR, MN, SC):
    decyear_final = YR + (MO-1)/12 + (DY-1)/365.25+ HR/(365.25*24) + MN/(365.25*24*60) + SC/(365.25*24*3600)
    return(decyear_final)

#=============================================================================
# 1.C
#=============================================================================
#                      define parameters  
#=============================================================================
# for seism rate
k_win    = 100
binsize  = 10 # for histogram

#  variables
t0     = float( ) # starting time of time axis
aT     = np.array([]) # time of seismicity
aMag   = np.array([]) # magnitudes
aT_inj = np.array([]) # time of injections
aV     = np.array([]) # injected volume
#aBin,aRate = np.array([]), np.array([]) # bins and seismicity rates

catName   = 'KTB'
dataDir   = '../data'

magFile   = 'KTB_mag.txt'
injFile   = 'KTB_inject.txt'

plotFile  = 'KTB_rate.png'

dpar  =  {  'showRate'  : True,
            'dt_map'    : 6./12, # time step for plotting eq and wells in map view
             'k'        : 200,  # for rate computation
             'tmin'     : 2005, 
              # basemap params
             'xmin'     : -101, 'xmax' : -94,  # basemap params
             'ymin'     :   33.5, 
             'ymax'     :  37.1,
             'projection' : 'merc',
             'lon'      : data2[7,:],
             'lat'      : data2[8,:]
           }


#===================================================================================
#                       load data
#====================================================================================

#taken from 3_4_KTB_rates-1.py
#magnitudes
mData = np.loadtxt( magFile, comments = '#').T #loads files named in 1.C
aT,aMag = mData[0], mData[1] #defines aT, aMag

#injection rate
mData = np.loadtxt( injFile, comments = '#').T #loads files named in 1.C
aT_inj, aV  = mData[3], mData[4] #defines aT_inj and aV

#substract initial t0 from both time vectors
if aT_inj[0] < aT[0]: 
    t0 = aT_inj[0]
else: 
    t0 = aT[0]
aT_inj, aT = (aT_inj - t0)/3600, (aT - t0)/3600 #convert to hr
#define new t0 in new time coordiante system in hr 
t0 = np.array([aT_inj[0], aT[0]]).min()



#=============================================================================
#                      rate computation   
#=============================================================================
## plot rate and cumulative number of events
if dpar['showRate'] == True:
    plt.figure(1)
    ax = plt.subplot( 211)
    #compute seismicity rates using eqRate from seis_utils
    seisrates = eqRate(aT, k_win)[1]
    time      = eqRate(aT, k_win)[0]
    #plot seismicity rates
    ax.plot(time, seisrates, 'r-')
    ax.set_ylabel( 'Earthquake Rate [ev/mo]')
    #plot cumulative number of earthquakes
    ax2 = plt.subplot( 212)
    cumearth = np.cumsum(np.ones(2304, dtype=float, order='C'))
    ax2.plot(time, cumearth)
    ax2.set_xlabel( 'Time [dec. yr]')
    ax2.set_ylabel('Cumulative Number')
    ax2.set_xlim( ax.get_xlim())
    plt.show()

#=============================================================================
# 1.D
#=============================================================================
#                       map view of well and event locations
#=============================================================================
# create time vector with dt_map spacing
at_bin  = np.arange( dpar['tmin'], 2018, dpar['dt_map'])
mSeis  = np.loadtxt( file2).T
aTime  = decyear(YR, MO, DY, HR, MN, SC)
mSeis  = np.array( [aTime, mSeis[7], mSeis[8], mSeis[-1]])
for i in range( at_bin.shape[0]-1):
    t1, t2 = at_bin[i], at_bin[i+1]
    #select earthquakes between t1 and t2 use np.logical_and
    sel_eq = np.logical_and( mSeis[0]  >= t1, mSeis[0]   < t2)
    #select wells with start dates before t1
    sel_we = np.logical_and( 0, mSeis[0]  >= t1)
    print (t1, t2, 'No. earthquakes', sel_eq.sum(), 'No. of wells', sel_we.sum())
    #create basemap object
    plt.figure(2)
    plt.cla()
    ax2 = plt.subplot(111)
    lon_0, lat_0 = .5*( dpar['xmin']+dpar['xmax']), .5*( dpar['ymin']+dpar['ymax'])
    m = Basemap(llcrnrlon = dpar['xmin'], urcrnrlon=dpar['xmax'],
                llcrnrlat = dpar['ymin'], urcrnrlat=dpar['ymax'],
                lon_0 = lon_0, lat_0 = lat_0, resolution = '1',
                 projection=dpar['projection'])
    #draw state boundaries
    m.drawstates()
    #plot seismicity and well locations
    #plot wells
    x,y = map(aTime, mWells)
    map.plot(x, y, 'bo', markersize=24)
    #plot seismicity
    x,y = map(aTime, mSeis)
    map.plot(x, y, 'ro', markersize=24)
    # x and y labels
    m.drawparallels( np.arange( 33,   38,  1), fmt='%i',labels=[1,0,0,0])
    m.drawmeridians( np.arange(-100,  -92, 2), fmt='%i',labels=[0,0,0,1])
    #marks points at time intreval given
    plt.pause( .5)
    
#=============================================================================
# 1.E
#=============================================================================
#      From your analysis of earthquake rates and locations, in what year did 
#      seismicityrates start to significantly exceed historic values?
#      When did earthquake rates start to again decrease?
#      Can you speculate on why?
#=============================================================================    
#it seems like in 6000 decyears, the seismiscity rates increased signigicantly.
# the rates seem to continue decreasing in spikes so it reaches a peak and then
# decreases right before increasing even more.
# This may have to do with the increase of well location sites.
    
    
