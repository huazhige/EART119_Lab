#Problem 1

"""
#Part A

"""
import numpy as np
from mpl_toolkits.basemap import Basemap

injWell_OK = 'injWell_OK.txt'

injection_wells = np.loadtxt(injWell_OK).transpose()
                #Reads info from injWell_OK.txt

seism_OK = 'seism_OK.txt'

seismic_activity = np.loadtxt(seism_OK).transpose()
                #Reads info from seism_OK.txt

"""
#Part B
"""

ID = []             #Making empty lists
YR = []
MO = []
DY = []
HR = []
MN = []
SC = []
lon = []
lat = []
depth = []
MAG = []
DecYear = []

for i in range(len(seismic_activity[0])):       
#Loop from i = 0 to the end of the length of seismic_activity
    ID.append(seismic_activity[0][i])           #Adding ith index of each list to the end of the respective list
    YR.append(seismic_activity[1][i])
    MO.append(seismic_activity[2][i])
    DY.append(seismic_activity[3][i])
    HR.append(seismic_activity[4][i])
    MN.append(seismic_activity[5][i])
    SC.append(seismic_activity[6][i])
    lon.append(seismic_activity[7][i])
    lat.append(seismic_activity[8][i])
    depth.append(seismic_activity[9][i])
    MAG.append(seismic_activity[10][i])
    DecYear.append(YR[i] + ((MO[i])-1)/12 + ((DY[i])-1)/365.25 + (HR[i])/(365.25*24) + (MN[i])/(365.25*24*60) + (SC[i])/(365.25*24*3600))
    #function given calculates decimal year and adds it to the end of the list
print(DecYear)

"""
Part C
"""
import matplotlib
seis_utils = '/Users/mikaballmer/Documents/UCSC/Astro 119/Hw2.py/seis_utils.py'

dPar = {'showRate'  :True,
        'dt_map'    : 6./12, #time step for plotting earthquakes and wells 
        #for rate computations
        'k'         : 200,
        'tmin'      : 2005,
        #basemap parameters
        'xmin'      : -101, 'xmax' : -94,
        'ymin'      : 33.5, 'ymax' :37.1,
        'projection': 'merc'              }

if dPar['showRate'] == True:
    matplotlib.figure(1)
    ax = matplotlib.subplot(211)

#Earthquake Rate
at = DecYear
k = 200
def earthquake_rates( at, k):
    aS = np.arrange(0, at.shape[0]-k, 1)
    aBin, aRate = np.zeros(aS.shape[0]), np.zeros(aS.shape[0])
    iS = 0
    for s in aS:
        i1, i2 = s, s+k
        aBin[iS] = 0.5*(at[i1]+at[i2])
        aRate[iS] = k/(at[i2]-at[i1])
        iS += 1
    return aBin, aRate
   
aBin = earthquake_rates(at,k)[0]
aRate = earthquake_rates(at,k)[1]
    
#Cumulative number
cum_num = np.cumsum(np.ones(7000))
    
#plot seismicity rates

matplotlib.plot(aBin, aRate)
    
ax.set_ylabel('Earthquake Rate [ev/mo]')
    
#plot cumulative number of earthquakes

matplotlib.subplot(212)
matplotlib.plot(aBin, cum_num)
matplotlib.xlabel('Time [decimal years]')
matplotlib.ylabel('Cumulative Number')
matplotlib.set_xlim(ax.get_xlim())
matplotlib.show()

"""
Part D
"""
seismic_activity = np.array([at,seismic_activity[7], seismic_activity[8], 
                             seismic_activity[-1]])
injection_wells = np.loadtxt(injWell_OK.txt).T

at_bin = np.arange(dPar['tmin'], 2018, dPar['dt_map'])
for i in range(at_bin.shape[0]-1):
    t1, t2 = at_bin[i], at_bin[i+1]
    sel_eq = np.logical_and(seismic_activity[0] >= t1, seismic_activity[0] <t2)
    sel_we = np.logical_and(injection_wells[1] <= t1, injection_wells[1] <t1)
    print(t1, t2, 'No. earthquakes', sel_eq.sum(), 'No. of wells', sel_we.sum())
    
    
    #create basemap object
    matplotlib.figure(2)
    matplotlib.cla()
    ax2 = matplotlib.subplot(111)
    lon_0, lat_0 = .5*(dPar['xmin']+dPar['xmax']), .5*(dPar['ymin']+dPar['ymax'])
    m = Basemap(llcrnrlon = dPar['xmin'], urcrnrlon = dPar['xmax'], 
                llcrnrlat = dPar['ymin'], urcrnrlat = dPar['ymax'],lon_0 = lon_0, 
                lat_0 = lat_0, resolution = 'l',
                projection = dPar['projection'], )

m.drawcoastlines()
aX_we, aY_we = m(injection_wells[2][sel_we], injection_wells[3][sel_we])
m.plot(aX_we, aY_we, 'go', ms = 2)
aX_eq, aY_eq = m(seismic_activity[1][sel_eq], seismic_activity[2][sel_eq])
m.plot(aX_eq, aY_eq, 'ro', ms = 2)
m.drawparallels(np.arange(33, 38, 1),    fmt='%i', labels=[1,0,0,0])
m.drawmeridians(np.arange(-100, -92, 2), fmt='%i', labels=[0,0,0,1])

matplotlib.pause(.5)
matplotlib.clf()

"""
Part E
"""
"""
Based on my analysis of earthquake rates and locations, seismicity rates 
started to significanty exceed historic values in the year 2010. In 
2017, earthquake rates started to decrease. This is beacause 
man-made earthquakes were no longer happening.
"""
