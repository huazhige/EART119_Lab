# -*- coding: utf-8 -*-
import os
import numpy as np
import matplotlib.pyplot as plt


"""
k/t(i+k)-t(i) ; i = 0...N-k
k=200
N = 7200
"""
# Load Data and Files
injFile = 'injWell_OK.txt'
seismFile = 'seism_OK.txt'

# Define Variables==============================
n      = 7200
k      = 200

mData = np.loadtxt( seismFile, comments = '#').T
YR,MO,DY,HR,MN,SC = mData[1], mData[2], mData[3], mData[4], mData[5], mData[6]

# Define functions====================================
def decYr(Yr, Mo, Dy, Hr, Mn, Sc):
    return YR + (MO-1)/12 + (DY-1)/365.25+ HR/(365.25) + MN/(365.25*24*60) 
    + SC/(365.25*24*3600)

#===============================================================
a_t = decYr(mData[1], mData[2], mData[3], mData[4], mData[5], mData[6])

def comp_rate( a_t, k):
    # smoothed rate from overlapping sample windows normalized by delta_t
    aS    = np.arange( 0, a_t.shape[0]-k, 1)
    rate = np.zeros(aS.shape[0])
    iS = 0
    for s in aS:
        i1, i2 = s, s+k
        rate[iS] = (k/( a_t[i2]-a_t[i1]))
        iS += 1
    return rate
    print('rate of ', a_t, '=', rate)






"""def comp_rate( DecMo, k):
    # smoothed rate from overlapping sample windows normalized by delta_t
    aS          = np.arange( 0, DecMo.shape[0]-k, 1)
    aBin, aRate = np.zeros(aS.shape[0]), np.zeros(aS.shape[0])
    iS = 0
    
    return aBin, aRate"""










  
