# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 10:53:33 2019

@author: Jason


1.Earthquake rates, earthquake and well locations in map-view(30 points)a)Load the two data filesinjWell_OK.txtand seism_OK.txt 
using the numpy method numpy.loadtxt. Note that by default numpy loads the data as column vectors analogous to matlab. To convert 
this into a more standard python format you will have to transpose thedata matrix.b)Convert the date-time columns to decimal years 
using:a.DecYear = YR + (MO-1)/12 + (DY-1)/365.25+ HR/(365.25*24) + MN/(365.25*24*60) + SC/(365.25*24*3600). You can write this into 
a separate function in a stand alone module so it can be used easily in future homework assignments.c)Determine earthquake rate. 
You can use the function we created in class with k=200or use plt.hist for which you have to create a monthly binned time vector 
as second input variable. Determine thecumulative number(use np.cumsum( np.ones( N)))of earthquakesand plot everythingas a function 
oftimeon two different subplots.d)Plot active wells(select wells with start dates before the beginning of the current time window)
and earthquakeswithin Dt=6months. Write a for loop that updates the current time window so it goes from2005 to2018( take a look at 
np.logical_and to select events within Dt).Instead of saving each figure and creating an animation with an external software, you can 
simply use plt.pause( <time interval>) to create an animation at run time when your script isexecuted.e)From your analysis of earthquake 
rates and locations, in what year did seismicityrates start to significantly exceed historic values?When did earthquake rates start to 
again decrease? Can you speculate on why?

python 2.7

rough homework!
"""

###############################################################################
#                           Imports and Libraries
###############################################################################
from __future__ import division
from mpl_toolkits.basemap import Basemap
import os
import numpy as np
import matplotlib.pyplot as plt


###############################################################################
#                           File and Variables and Functions
###############################################################################

file_in_inj = 'injWell_OK.txt'
file_in_sei = 'seism_OK.txt'

dPar = {    'showRate' : True,
        'dt_map' : 6./12,
        'k' : 200,
        'tmin' : 2005,
        'xmin' : -101, 'xmax' : -94,
        'ymin' : 33, 'ymax' : 37,
        'projection' : 'merc', 
        }


def DecYear(Yr, Mo, Dy, Hr, Mn, Sc):
    return Yr + ((Mo - 1)/(12)) + ((Dy - 1)/(365.25)) + (Hr/(365.25)) + (Mn/(365.25*24*60)) + (Sc/(365.25*24*3600))
    
    






###############################################################################
#                           loading Data
###############################################################################

    

seisData = np.loadtxt(file_in_sei).T
#print(injData)
#print(seisData)


YR = seisData[1]
#print(YR)
MO = seisData[2]
#print(MO)
DY = seisData[3]
#print(DY)
HR = seisData[4]
#print(HR)
MN = seisData[5]
#print(MN)
SC = seisData[6]
#print(SC)


seisData = ([DecYear(YR, MO, DY, HR, MN, SC), seisData[7], seisData[8], seisData[-1]])
#print DecYear(YR, MO, DY, HR, MN, SC), this works

#plt.hist(DecYear(YR, MO, DY, HR, MN, SC), normed = True, bins = 1000)
#plt.show()
injData = np.loadtxt(file_in_inj).T

print(seisData)

###############################################################################
#                           earthquake rates, cumulative number
###############################################################################

if dPar['showRate'] == True:
    plt.figure(1)
    ax = plt.subplot( 211)
    
    ax.set_ylabel( 'Earthquake Rate [ev/mo]')
    ax2 = plt.subplot( 212)
    
    ax2.set_xlabel( 'Time [dec. yr]')
    ax2.set_ylabel( 'Cumulative Number')
    ax2.set_xlim( ax.get_xlim())
    plt.show()
    

###############################################################################
#                           map view of well and event location
###############################################################################

at_bin = np.range(dPar['tmin'], 2018, dPar['dt_map'])
for i in range( at_bin.shape[0]-1):
    t1, t2 = at_bin[i], at_bin[i+1]
    #TODO: select earthquakes between t1 and t2 use np.logical_and
    sel_eq = np.logical_and( seisData[0]  >= t1, seisData[0]   < t2)
    #TODO: select wells with start dates before t2
    sel_we = np.logical_and(injData[-1]  >= t1, injData[-1]   < t2)
    
    
    
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
    m.drawstates(linewidth = 0.5)
