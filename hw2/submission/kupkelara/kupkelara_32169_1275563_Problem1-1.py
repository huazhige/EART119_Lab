#!Python 2.7

"""Homework #2:"""

#import
import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

#=================
#Part a
#=================
#load the data and transpose it

#data directory
DATA_DIR = './'

#load
os.chdir(DATA_DIR)
FILE_INJ = 'injWell_OK.txt'
FILE_SEISM = 'seism_OK.txt'
DATA_INJ = np.loadtxt(FILE_INJ, comments='#').T
DATA_SEISM = np.loadtxt(FILE_SEISM, comments='#').T

#=================
#functions
#=================
#convert date-time collumns to decimal years

def conv_dec_years(YR, MO, DY, HR, MN, SC):
    """Convert input from decimals to years."""
    return YR + (MO-1)/12 + (DY-1)/365.25+ HR/(365.25) + MN/(365.25*24*60) + SC/(365.25*24*3600)

def seismic_rates(months, k_win): #taken from in class
    """Compute earthquake rate. Smoothed rates from sample windows"""
    aS = np.arange( 0, months.shape[0]-k_win, 1)
    month_bin, month_rate = np.zeros(aS.shape[0]), np.zeros(aS.shape[0])
    counter = 0
    for s in aS:
        i1, i2 = s, s+k_win
        month_bin[counter] = 0.5*(months[i1]+ months[i2])
        month_rate[counter] = k_win/(months[i2]- months[i1])
        counter += 1
    return month_bin, month_rate

#part a
YEAR_SEISM = np.array([conv_dec_years(DATA_SEISM[1], DATA_SEISM[2], DATA_SEISM[3], DATA_SEISM[4], DATA_SEISM[5], DATA_SEISM[6])]).T

DATA_SEISM = np.delete(DATA_SEISM, np.s_[1:5], 1)
DATA_SEISM = np.insert(DATA_SEISM, 1, YEAR_SEISM, axis=1)

#Earth quake rate and cummulative sum
years = np.array([.5])
k_win = 200
MONTHS, RATE = seismic_rates(years, k_win)


Cum_quakes = np.cumsum(DATA_SEISM[:,1])

plt.figure(1)
ax1 = plt.subplot( 211)
ax1.plot(MONTHS, RATE, 'b-')
ax1.set_ylabel( 'Earthquake Rate [ev/mo]')
ax2 = plt.subplot( 212)
ax2.plot(DATA_SEISM[:,1],Cum_quakes,'ko')
plt.show()


#From your analysis of earthquake rates and locations, in what year did seismicity rates start to significantly exceed historic values?When did earthquake rates start to again decrease? Can you speculate on why?

