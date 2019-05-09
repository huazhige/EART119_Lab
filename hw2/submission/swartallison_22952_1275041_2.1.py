# Allison Swart
# Astro/Earth 119 Homework #2
# April 23, 2019

#anaconda2/python2.7

import numpy as np
import matplotlib.pyplot as plt

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#            Problem 1
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# PART A

file_one = 'Wells.txt'
file_two = 'Seism.txt'

Wells = np.loadtxt( file_one).T
Seism = np.loadtxt( file_two).T

# PART B

SC = Seism[6] 
MN = Seism[5] 
HR = Seism[4]
DY = Seism[3]
MO = Seism[2]
YR = Seism[1]

DecYear = YR + (MO-1)/12 + (DY-1)/365.25 + HR/(365.25) + MN/(365.25*24*60) + SC/(365.25*24*3600)

print 'Decimal Year =', DecYear

# PART C

dPar = { 'nClicks': 10, 'tmin': 2010, 'area_OK': 181*1e3, 
        'xmin': -101, 'xmax': -94, 'ymin': 33.5, 'ymax': 37.1, 
        'projection': 'aea'}   #km

def earthquake_rate( a_t, k):
     aS = np.arange( 0, a_t.shape[0]-k, 1)
     a_bin = np.zeros( aS.shape[0])
     a_rate = np.zeros( aS.shape[0])
     iS = 0
     for s_step in aS:
        i1, i2 = s_step, s_step+k
        a_rate[iS] = k/(a_t[i2] - a_t[i1])
        a_bin[iS] = 0.5*( a_t[i1] + a_t[i2])
        iS += 1
     return a_bin, a_rate
 

aT = DecYear
k_win = 200
a_tbin, a_rate = earthquake_rate( aT, k_win)
print a_rate


N = len( Seism[10])
np.cumsum( np.ones( N))
print np.cumsum( np.ones( N))

plt.figure(1)
plt.subplot(111)
plt.plot( Seism[1], Seism[10], 'bo', ms = 4)
plt.xlabel( 'Time [yrs]')
plt.ylabel( 'Magnitude')

plt.figure(2)
plt.subplot(212)
plt.plot( Wells[1], Wells[4], 'go', ms = 3)
plt.xlabel('Time [yrs]')
plt.ylabel( 'Volume [m^3]')
plt.show()

# PART E
"""
After 2010, earthquake rates started to significantly exceed historical 
values. They then started to decrease again in 2012 or 2013. This likely
is because of an increase and then decrease in the amount of material
injected by humans into the ground. Comparing the two plots, it is easy
see an increase in magnitude of earthquakes that corresponds to an 
increase in well activity.
"""
