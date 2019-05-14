# -*- coding: utf-8 -*-
"""
Created on Apr 21, 2019
Class = Astro/Eart 119
Homework 2 - Plots and Animations
Student = Benjamin Zhu (1696575)

"""
#============================================
#           (a) imports
#============================================
import numpy as np

injWell = np.loadtxt('injWell_OK.txt').T  #import the txt file while transposing them
seism   = np.loadtxt('seism_OK.txt').T

#============================================
#           (b) Convert to decimal years
#============================================

Yr  = seism[1:2]    #assigning the row of data files to their variables
Mo  = seism[2:3]
Dy  = seism[3:4]
Hr  = seism[4:5]
Mn  = seism[5:6]
Sc  = seism[6:7]

DecYear = Yr + (Mo-1)/12 + (Dy-1)/365.25 + Hr/(365.25*24) +\
Mn/(365.25*24*60) + Sc/(365.25*24*3600)   #calculations

print(DecYear)

#============================================
#           (c) calculate earth quake rate (not solved)
#============================================
"""
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
#===================================================================================
#                         dir, file, and parameter
#===================================================================================
# for seism rate
k_win    = 200
binsize  = 10 # for histogram

#  variables
t0     = float( ) # starting time of time axis
at     = np.array([]) # time of seismicity
aMag   = np.array([]) # magnitudes
aT_inj = np.array([]) # time of injections
aV     = np.array([]) # injected volume
#aBin,aRate = np.array([]), np.array([]) # bins and seismicity rates

answer = comp_rate(at, k_win)
print (answer)
"""
#============================================
#           
#============================================



#============================================
#           
#============================================



