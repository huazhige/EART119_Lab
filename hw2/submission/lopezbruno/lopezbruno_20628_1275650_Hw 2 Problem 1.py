# -*- coding: utf-8 -*-
"""
This is Using the Files Prof. Goebel gave us,I just put it on a different doc 
to be easy to read

"""

#====================0=================
#===============Variables, Functions, files###############
#========================================================

from __future__ import division
import os
import matplotlib.pyplot as plt
#from matplotlib
import numpy as np

#Loads the seism_OK file
file_eq = 'seism_OK.txt'
#Loads the file_well file
file_well = 'injWell_OK.txt'

#Working directory
os.chdir("./")
# load seismicity and well data using loadtxt
mSeis  = np.loadtxt( file_eq, comments = "#").T

                    #Function to convert into decimal years
def decimalToYear(Year, Month, Day, Hour, minute, second):
    return Year + ((Month - 1)/12) + ((Day-1)/365.25) + (Hour/(365.25*24))  \
+ (minute /(365.25*24*60)) + (second/(365.25*24*3600))

#Function to find the rate of earthquakes
def comp_rate( at, k_win):
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





K = 200 #K window
yr = mSeis[1] # Years
month = mSeis[2] #Months
day = mSeis[3] #Day
hour = mSeis[4] #Hour
minute = mSeis[5] #Minute
second = mSeis[6] #Second
#Converts the data to decimal years
aT = decimalToYear(yr,month,day,hour,minute,second)
time_min = 2005 #MIn time for the injection wells
dt_map = 0.5 #Time interval

mSeis = np.array( [aT, mSeis[7], mSeis[8], mSeis[-1]]) #Makes an array of the neccesary data

mWells = np.loadtxt('injWell_OK.txt', comments = '#').T #Loads well data
                 
#Makes a plot of earthquake rate vs time                   
plt.figure(1)
ax = plt.subplot(211)
seis_rate = comp_rate(aT,K)
seis_rate1 = np.asarray(seis_rate)
plt.plot(seis_rate[0], seis_rate[1])
ax.set_ylabel( 'Earthquake Rate [ev/mo]')

#Finds the sum of earthquakes, had a hardtime with numsum
z = np.sum(seis_rate[1])

#Plots the cumulative sum of earthquakes vs time
ax2 = plt.subplot(212)
plt.plot(seis_rate[0], z)
ax2.set_xlabel( 'Time [dec. yr]')
ax2.set_ylabel('Cumulative Number')



#Sets thg boundaries for the well
at_bin  = np.arange( time_min, 2018, dt_map)
for i in range( at_bin.shape[0]-1):
    t1, t2 = at_bin[i], at_bin[i+1]
    sel_eq = np.logical_and( mSeis[0]  >= t1, mSeis[0]   < t2)
    #TODO: select wells with start dates before t1
    inj_wells = mWells[1] < 2005
    sum_wells = inj_wells.sum()
    print(t1, t2, 'No. earthquakes', sel_eq.sum(), 'No. of wells', sum_wells)
    ### create basemap object
    plt.figure(2)
    plt.cla()
    ax3 = plt.subplot(111)









                    









