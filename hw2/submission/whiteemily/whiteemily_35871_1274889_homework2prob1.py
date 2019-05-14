# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 17:13:56 2019

@author: Emily White
"""

"""

    Earthquake rates, earthquake and well locations in map-view

"""
#=============================================================================
#               imports
#=============================================================================
import numpy as np
import os
import matplotlib.pyplot as plt #from matplotlib

from mpl_toolkits.basemap import Basemap

#my modules
import seis_utils
    
#=============================================================================
#           files/dir and params
#=============================================================================
k_win = 200
binsize = 20 #for histogram

""" variables """
t0      = float()       # start time
aT      = np.array([])  # time of seismicity
aLoc    = np.array([])  # magnitudes 
aT_inj  = np.array([])  # time of injections
aV      = np.array([])  # volume injected



dataDir ='./'

injWell = 'injWell_OK.txt'
seism = 'seism_OK.txt'

plotFile = 'homework2prob1.png'

#=============================================================================
#               load data
#=============================================================================
os.chdir(dataDir)
locData = np.loadtxt(injWell).T
aT,aLoc = locData[0], locData[1]

dPar = { 'showRate' : True,
        'dt_map' : 6./12,
        'k' : 200,
        'tmin' : 2005,
        'xmin' : -101, 'xmax' : -94,
        'ymin' : 33.5, 'ymax' : 37.1,
        'projection' : 'merc' }
   
def dateTime2decYr(YR, MO, DY, HR, MN, SC):
    nDays = 365.25
    return YR + (MO - 1)/12 + (DY - 1)/nDays + HR/(nDays*24) + MN/(nDays*24*60) + SC/(nDays*24*3600)

sData = np.loadtxt(seism).T
sData = np.array([aT, sData[7], sData[8], sData[-1]])



#=============================================================================
#                   eartquake rates, cumul #
#=============================================================================#=============================================================================

if dPar['showRate'] == True:
    plt.figure(1)
    ax = plt.subplot(211)
    
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

    ax.set_ylabel('Eartquake Rate [ev/mo]')
    ax2 = plt.subplot(212)
    
    ax2data = np.random.randn(200)
    ax2hist, base = np.histogram(ax2data, bins = 20)
    ax2cumulative = np.cumsum(ax2hist)
    plt.plot(base[:-1], ax2cumulative, c='blue')
    plt.plot(base[:-1], len(ax2data)-ax2cumulative, c='green')
    plot.show()
    
    
    ax2.set_xlabel('Time [dec. yr]')
    ax2.set_ylabel('Cumulative Number')
    ax2.set_xlim(ax.get_xlim())
    plt.show()
    
    
#========================================
    
#========================================
at_bin = np.arange(dPar['tmin'], 2018, dPar['dt_map'])
for i in range(at_bin.shape[0]-1):
    t1,t2 = at_bin[i], at_bin[i+1]
    np.logical_and
    sel_eq = np.logical_and(sData[0] >= t1, sData[0] < t2)
    
    def beforet1():
        print('t1')
    
    t = Timer(t1, beforet1)
    t.start()

    print(t1, t2, 'Number earthquakes', sel_eq.sum(), 'Number of wells', sel_we.sum())
    # create basemap object
    plt.figure(2)
    plt.cla()
    ax2 = plt.subplot(111)
    lon_0, lat_0 = (dPar['xmin']+dPar['xmax'])/2 , (dPar['ymin']+dPar['ymax'])/2
    m = Basemap(llcrnrlon = dPar['xmin'], urcrnrlon = dPar['xmax'], llcrnrlat = dPar['ymin'],  
                urcrnrlat = dPar['ymax'], lon_0 = lon_0, lat_0 = lat_0, resolution = 'l', 
                projection = dPar['projection'])
    #draw state boundaries
    m.drawstates()
    m.drawcountries()
    m.drawcoastlines()
    m.drawmapboundary(fill_color='aqua')
    m.fillcontinents(color='brown', lake_color='aqua')
    plt.show()
    
    #convert spherical to 2D coord system in basemap
    fig = plt.figure(figsize = (8,8))
    m = Basemap(projection='lcc', resolution = None, width=8e6, height=8e6,
                lat_0=lat_0, lon_0=lon_0)
    
    
    #plot semismicity and well locations
    parallels = np.arange(33, 38, 1)
    meridians = np.arange(-100,-92, 2)
    lats = m.drawparallels(np.linspace(33, 38, 1))
    lons = m.drawmeridians(np.linspace(-100, -92, 2))
    
    # x & y labels
    m.drawparallels(np.arange(33, 38, 1), fmt= '%i', labels=[1,0,0,0])
    m.drawmeridians(np.arange(-100,-92, 2), fmt= '%i', labels=[0,0,0,1])


    file_out = 'OK_seis_t_%.1f_%.1f.png'%(t1,t2)
    plt.savefig(file_out, dpi = 150)
    plt.clf()
    
    plt.pause(.5)













#=============================================================================
