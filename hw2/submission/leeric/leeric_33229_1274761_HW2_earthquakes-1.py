# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 19:06:02 2019
Homework #2 Astro 119
@author: eric_
"""
#============================================================
#  problem 1 earthquake rates, earthquake and well locations
#============================================================
import numpy as np
import matplotlib.pyplot as plt

Well_file = 'injWell_OK.txt'  #data files
Seism_file = 'seism_OK.txt'

#=============================================================
#                   load data
#=============================================================
Well_data = np.loadtxt(Well_file).T
Seism_data = np.loadtxt(Seism_file).T

#change date-time columns to decimal years
DecYear = Seism_data[1] + ((Seism_data[2]-1)/12)  + ((Seism_data[3]-1)/365.25)\
+ (Seism_data[4]/(365.25*24)) + (Seism_data[5]/(365.25*24*60)) +\
 (Seism_data[6]/(365.25*24*3600))



#================================================================
#                   comp rate function
#================================================================
k_win = 200
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

#================================================================
#                  earthquake rate plot 
#================================================================\
#Using histograms
aBin, aRate = comp_rate(DecYear, k_win)
binsize = 1/12
aHistBins = np.arange(DecYear[0], DecYear[-1], (binsize))
aN_bin, aHistBins = np.histogram(DecYear, bins = aHistBins)
aN_bin = aN_bin/binsize
plt.figure(3)
plt.title("Earthquake rate")

earthquake_rate = plt.subplot(211)
earthquake_rate.set_title("Using Histogram")
earthquake_rate.set_xlim(1973, 2020)
earthquake_rate.set_xlabel("Time (yrs)")
earthquake_rate.set_ylabel("Number of Earthquakes")
earthquake_rate = plt.plot( aHistBins[0:-1]+.5*binsize, aN_bin, 'ko')


#using comp rate funciton
axis1 = plt.subplot(212)
axis1.set_title("Using Comp Rate")
axis1.plot(aBin, aRate, 'ko', lw = .1, ms = 1)
axis1.set_xlabel("Time (yrs)"), axis1.set_ylabel("Number of Earthquakes")
axis1.set_xlim(1973, 2020)
plt.show()

#=================================================================
#           plot active wells
#=================================================================
year_vector = np.genfromtxt(Well_file, skip_header = 1, usecols= (1), dtype = \
                            float)
#print(year_vector)
sort_id = year_vector.argsort()
year_vector = year_vector[sort_id]

#=================================================================
#           for loop active wells
#=================================================================
sel_eq = 0
sel_eq2 = 0
for i in np.arange(2005, 2013, 1): 
    sel_eq = 0
    sel_eq2 = 0
    for it in range(np.shape(year_vector)[0]):
        if year_vector[it] > i and year_vector[it] < i + 0.5:
            sel_eq = sel_eq + 1
        var1 = sel_eq
        if year_vector[it] > i + 0.5 and year_vector[it] < i + 1:
            sel_eq2 = sel_eq2 + 1
        var2 = sel_eq2
    print("Number of active wells between Jan", i, "- June", i, ": ", var1)
        
    print("Number of active wells between July", i, "- December", i, ": ", \
          var2)
    plt.figure(4000)
    plt.title(i)
    subplot_1 = plt.subplot(211)
    First_histo = plt.hist(var1, 1)
    subplot_2 = plt.subplot(212)
    Second_histo = plt.hist(var2, 1)
        #plt.show
    plt.pause(0.5)
    plt.clf


#=================================================================
#           earthquakes from 2005 to 2018
#=================================================================
num_earthquakes = 0
num_earthquakes2 = 0
for element in np.arange(2005, 2018, 0.5):
    num_earthquakes = 0
    num_earthquakes2 = 0
    var3 = 0
    var4 = 0
    for it in range(np.shape(DecYear)[0]):
        if DecYear[it] > element and DecYear[it] < element + 0.5:
            num_earthquakes += 1
        var3 = num_earthquakes
        if DecYear[it] > element + 0.5 and DecYear[it] < element + 1:
            num_earthquakes2 += 1
        var4 = num_earthquakes2
    plt.figure(5000)
    plt.title(element)
    e_subplot_1 = plt.subplot(211)
    e_First_histo = plt.hist(var3, 1)
    e_subplot_2 = plt.subplot(212)
    e_Second_histo = plt.hist(var4, 1)
    plt.pause(0.5)
    plt.clf
    


#earthquakes seem to spike in 2013
        
        
"""for it in np.unique(year_vector):
    if it > 2004 and it < it + 0.5:
        sel_eq = it == year_vector
        print("it= ", it, "sel_eq.sum() = ", sel_eq.sum())
    elif it > 2004 and it > it + 0.5:
        sel_eq2 = it == year_vector
        print("it2 = ", it, "sel_eq2.sum() = ", sel_eq2.sum())"""


"""for it in np.unique(year_vector):
    if it > 2004:
        sel_eq3 = it == year_vector
        print("current year", it, "#no of active wells: ", sel_eq3.sum())
        plt.figure(2)
        subplot_1 = plt.subplot(211)
        subplot_1.set_xlim(0, 150)
        plt.hist(sel_eq3.sum(), 1)
        #plt.show
        plt.pause(0.5)
        plt.clf"""
              





