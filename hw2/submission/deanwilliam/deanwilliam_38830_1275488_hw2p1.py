#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 17:23:08 2019

@author: williamdean

HW2#1
"""
import os
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.basemap as Basemap
import seis_utils
#===============================
#  files and parameters
#===============================
data_dir = './'
file_sm = 'seism_OK.txt'
file_ij = 'injWell_OK.txt'

dPar  =  {  'showRate'  : True,'dt_map'    : 6./12, 
          # time step for plotting eq and wells in map view
          # for rate computations 
          'k': 200, 'tmin' : 2005, 
          # play with this number to visualize historic rates
          #       -----basemap params----------------------
          'xmin' : -101, 'xmax' : -94, 'ymin' : 33.5, 'ymax' :  37.1,
         'projection' : 'merc', # or 'aea' for equal area projections}
         }


#load data
os.chdir( data_dir)
# load seismicity and well data
mSeis = np.loadtxt( file_sm).T
aTime = 100
mSeis  = np.array( [aTime, mSeis[7], mSeis[8], mSeis[-1]])
mWells = np.loadtxt( file_ij).T
#========================
#earthquake rates
#=======================
if dPar['showRate'] == True:
    plt.figure(1)
    ax = plt.subplot( 211)
    # compute seismicity rates using seis_utils.eqRatarea_poly
    #seis_utils.eqRate( at, k_win)
    # smoothed rate from overlapping sample windows normalized by delta_t
def eq_rate( at, k_win):    
    aS          = np.arange( 0, at.shape[0] - k_win, 1)
    aBin, aRate = np.zeros(aS.shape[0]), np.zeros(aS.shape[0])
    iS = 0
    for s in aS:
        i1, i2 = s, s+k_win
        aBin[iS]  = 0.5*( at[i1]+at[i2])
        aRate[iS] = k_win/( at[i2]-at[i1])
        iS += 1
    return aBin, aRate
    #TODO: plot seismicity rates
    plt.plot( aBin, aRate)

ax.set_ylabel( 'Earthquake Rate [ev/mo]')
ax2 = plt.subplot( 212)
#TODO: plot cumulative number of earthquakes
ax = file_sm.plot( kind = 'line' )

ax2.set_xlabel( 'Time [dec. yr]')
ax2.set_ylabel('Cumulative Number')
ax2.set_xlim( ax.get_xlim())
plt.show()

#map view of well and event locations#------------------------------------------------------------------------
# create time vector with dt_map spacing 
at_bin  = np.arange( dPar['tmin'], 2018, dPar['dt_map'])
for i in range( at_bin.shape[0]-1):
    t1, t2 = at_bin[i], at_bin[i+1]
    #TODO: select earthquakes between t1 and t2 use np.logical_and 
    sel_sm = np.logical_and( mSeis[0]  >= t1, mSeis[0]   < t2)
    #TODO: select wells with start dates before t1
    sel_ij = np.logical_and( mWells[0] >= t1)
    print(t1, t2, 'No. earthquakes', sel_sm.sum(), 'No. of wells', sel_ij.sum())
    ### create basemap object
    plt.figure(2)
    plt.cla()
    ax2 = plt.subplot(111)
    lon_0, lat_0 = .5*( dPar['xmin']+dPar['xmax']), .5*( 
            dPar['ymin']+dPar['ymax'])
    m = Basemap( llcrnrlon = dPar['xmin'], urcrnrlon=dPar['xmax'],
                llcrnrlat = dPar['ymin'], urcrnrlat=dPar['ymax'],
                lon_0 = lon_0, lat_0 = lat_0,
                resolution = 'l',
                projection=dPar['projection'] )
    #TODO: draw state boundaries
m.drawcoastlines()
m.drawcountries()
m.drawstates()
    #TODO: convert spherical to 2D coordinate system using basemap
xpt,ypt = m(lon_0,lat_0)
# TODO: plot seismicity and well locations
plt.show()
# x and y labels
m.drawparallels( np.arange( 33,   38,  1), fmt='%i',labels=[1,0,0,0])
m.drawmeridians( np.arange(-100,  -92, 2), fmt='%i',labels=[0,0,0,1])
file_out = 'OK_seis_t_%.1f_%.1f.png'%( t1, t2)
plt.savefig(  file_out, dpi = 150)
plt.clf()
plt.pause( .5)

# extra stuff #
#array = pd.read_csv('data/seism_OK.txt', index_col=[0]).values

#def convert(YR, MO, DY, HR, MN, SC):
   # return (YR + (MO-1)/12 + (DY-1)/365.25 + HR/(365.25) + MN/(365.25*24*60) 
    #+ SC/(365.25*24*3600))
#seism = np.genfromtxt(file_sm, skip_header=1, delimiter= '  ', dtype=float)


#print(len(seism)) #sanity check
#print(len(seism[0]))
#print(seism[0])





#def comp_rate( at, k_win):
 #   aS          = np.arange( 0, at.shape[0]-k_win, 1)
 #   a_bin, a_rate = np.zeros(aS.shape[0]), np.zeros(aS.shape[0])
  #  iS = 0
  #  for s in aS:
   #     i1, i2 = s, s+k_win
    #    a_bin[iS]  = 0.5*( at[i1]+at[i2])
     #   a_rate[iS] = k_win/( at[i2]-at[i1])
     #   iS += 1
    #return a_bin, a_rate

#k_win = 200 #sample window
#
#np.cumsum( np.ones( N))
# print(len(seism[0]))
