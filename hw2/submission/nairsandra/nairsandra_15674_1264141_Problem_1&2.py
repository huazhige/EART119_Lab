# -*- coding: utf-8 -*-
#anaconda2, Python 2.7
"""
Earthquake rates, earthquake and well locations in map-view
    

"""

import os
os.environ['PROJ_LIB'] = r'C:\ProgramData\Anaconda2\pkgs\proj4-5.2.0-hc56fc5f_1\Library\Share'

import numpy as np
import matplotlib.pyplot as plt
#from mpl_toolkits.basemap import Basemap as Basemap

#=========================================================
#                   fncn def
#=========================================================
#test
'''
m = Basemap(width=12000000,height=9000000,projection='lcc',
            resolution=None,lat_1=45.,lat_2=55,lat_0=50,lon_0=-107.)
m.bluemarble()
plt.show()

'''


def comp_rate(a_t, k):
    """
    -compute rate change for vector a_t
    :input
            a_t = time vector
            k = sample window -> controls smoothness
    
    :output a_bin, a_rate
    
    """
    aS = np.arange(0, len(a_T)-k_win, 1)
    a_bin = np.zeros(aS.shape[0])
    a_rate = np.zeros(aS.shape[0])
    iS = 0
    for s_step in aS:
        i1, i2 = s_step, s_step+k
        a_rate[iS] = k/(a_t[i2]-a_t[i1])
        a_bin[iS] = 0.5*(a_t[i1]+a_t[i2])        
        iS += 1
    return a_bin, a_rate

#=========================================================
#             files   
#=========================================================
file_inj = 'injWell_OK.txt'
file_seism = 'seism_OK.txt'

#=========================================================
#              params and variables
#=========================================================
def date_in_dec(YR, MO, DY, HR, MN, SC):
    DecYear = YR + (MO-1)/12 + (DY-1)/365.25+ HR/(365.25*24) + MN/(365.25*24*60) + SC/(365.25*24*3600)
    return DecYear

k_win = 200


#=========================================================
#             load data and comp.rates
#=========================================================
mData = np.loadtxt(file_inj).T

nData = np.loadtxt(file_seism).T

seismX = file_seism[7, :] #longitudes of earthquakes
seismY = file_seism[8, :] #Latitudes of earthquakes
                   
wellX = file_inj[2,:] #longitudes of injection
wellY = file_inj[3,:] #latitudes of injections
well_time = file_inj[1,:] #times of injections

#stort Well cronologically, might want earlier well though
sort_id = well_time.argsort()
wellX = wellX[sort_id]
wellY = wellY[sort_id]
well_time = well_time[sort_id]

 

#create empty vector where stuff could be saved in

a_T = []

#Want to get the entries in first col, corresponding to variables that date_in_dec depends on; i.e., YR, MO, DY, HR, MN, SC
#a_T[0]=date_in_dec(nData[1,0], nData[2,0], nData[3,0], nData[4,0], nData[5,0], nData[6,0])

#need to repeat for cols from 0 to last col

#row, col = nData.shape
#According to variable explorere, our matrix for nData is 11X7200

for i in range(7200):
    temp = date_in_dec(nData[1,i], nData[2,i], nData[3,i], nData[4,i], nData[5,i], nData[6,i])

#need to glue on a spot to our empty vector, using append

    a_T.append(temp)



a_bin, a_rate = comp_rate(a_T, k_win)

#=========================================================
#             plots
#=========================================================

fig1 = plt.figure(1)
ax1 = plt.subplot(211)
ax1.plot(a_bin, a_rate, 'b-')
ax1.set_ylabel('Cumulative injection rate [m3]')
ax2 = plt.subplot(212)
ax2.plot(a_bin, np.cumsum(a_rate),'ko')
ax2.set_xlim(ax1.get_xlim())
plt.show


#Oklahomas latitudes
maxLon = -94
maxLat = 38
minLon =-103
minLat =33
lon_0, lat_0 = .5*( minLon + maxLon), .5*( minLat + maxLat)
m2 = Basemap(projection = 'cyl',
                llcrnrlon = minLon, urcrnrlon=maxLon,
                llcrnrlat = minLat, urcrnrlat=maxLat,
                 resolution = 'c', lon_0 = lon_0, lat_0 = lat_0)

for year in np.arange(2005, 2018.5, .5):
    quakes = [i for i in a_T if i>=year]
    Index_1 = len(a_T) - len(quakes)
    quakes = [i for i in quakes if i<=year+.5]
    Index_l = [Index_1] + len(quakes)-1
    
# is empty if Index_1>Index_l
    Index = np.arange(Index_1, Index_l, 1)    
    
# affected region

    wells = [i for i in well_time if i >= 2005]
    wIndex_1 = len(well_time)-len(wells)
    wells = [i for i in wells if i <= year+0.5]
    wIndex_l = wIndex_1+len(wells)-1
    
# is empty if wIndex_1>wIndex_l    
    wIndex = np.arange(wIndex_1, wIndex_l, 1)    
    
    plt.figure(2)
    plt.cla()
    plt.title( str( year))
    
'''
    #m.plot(  aX_eq, aY_eq, 'ro', ms = 6, mew = 1.5, mfc = 'none')
    plot1 =     plt.scatter( aX_eq, aY_eq, c = mLoc[2][sel_eq], s = np.exp( mLoc[2][sel_eq]-3))
    cbar  = plt.colorbar( plot1, orientation = 'horizontal')
    cbar.set_label( 'Magnitude')
    #--------------
    #plt.savefig(  file_out, dpi = 150)
    #
    plt.pause( .5)
    #plt.show()
    plt.clf()
'''


plt.title('Click 10 points encapsuling the area, click COUNTERCLOCKWISE')
tCoord = plt.ginput(4)
X = np.array(tCoord).T[0]
Y = np.array(tCoord).T[1]

plt.title('Selected Area')
m2.plot(X,Y, 'b')

    
eqX, eqY = m2(X,Y)
    
#define function again here
def area_polygon_vec(l_x, l_y):
    """
    - computes the area of polygon with vertices defined by 
    position vectors l_x and l_y
    
    :input
    l_x = the x-coordinates of the vertices
    l_y = the y-coordinates of the vertices in the same order as l_x
    
    :output
    A = the area of the polygon
    """
    x_N = len(l_x)
    y_N = len(l_y)
    
    if x_N != y_N:
        return -1
    else:
        l_y_shift = np.concatenate((l_y[1:y_N], l_y[0]),axis=None)
        x_sum = np.dot(l_x,l_y_shift, out=None) #elementwise multiplicaction
        
        l_x_shift = np.concatenate((l_x[1:x_N],l_x[0]),axis=None)
        y_sum = np.dot(l_y,l_x_shift, out=None)
        
        A = 0.5*abs(x_sum-y_sum)
        
        return A
    
Area = area_polygon_vec(eqX, eqY)
oakArea= 181000
print(Area)


ratio = 100*Area/oakArea
print(ratio)

titleName = 'the affected area is ' + str(Area) + ' km^2, which is ' + str(ratio) + '% of the total area of Oklahoma'
#image2.plt.title(titleName)
