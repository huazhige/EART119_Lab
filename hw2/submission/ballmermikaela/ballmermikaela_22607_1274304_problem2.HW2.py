#Problem 2
"""
Part A
"""
import matplotlib.pyplot as plt
import numpy as np
#from mpl_toolkits.basemap import Basemap


injWell_OK = 'injWell_OK.txt'
injection_wells = np.loadtxt(injWell_OK).transpose()
                #Reads info from injWell_OK.txt

seism_OK ='seism_OK.txt'
seismic_activity = np.loadtxt(seism_OK).transpose()
                #Reads info from seism_OK.txt
                
file_eq = 'seism_OK.txt'
file_well = 'injWell_OK.txt'

"""
converting to decimal years
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
 
dPar = { 'nclicks'    : 1,
         'tmin'       : 2010,
         'areaOK'     : 181*1e3, #in km
         'dt_map'     : 6./12,
         'xmin'       : -101, 'xmax' : -94,
         'ymin'       : 33.5, 'ymax' : 37.1,
         'projection' : 'aea'}

#seismicity boundaries
plt.figure(1)
ax1 = plt.subplot(111)

aT = DecYear
seismic_activity = np.array([aT, seismic_activity[7], seismic_activity[8], seismic_activity[-1]])
sel = np.logical_and(DecYear >= 2010, DecYear <= 2017)


print("Please click %i times"%(dPar['nclicks']))
tCoord = plt.ginput(dPar['nClicks'])
print("clicked", tCoord)
plt.show()

at_bin = np.arange(dPar['tmin'], 2018, dPar['dt_map'])
for i in range(at_bin.shape[0]-1):
    t1, t2 = at_bin[i], at_bin[i+1]
    sel_eq = np.logical_and(seismic_activity[0] >= t1, seismic_activity[0] < t2)
    sel_wells = np.logical_and(injection_wells[1] <= t1, injection_wells[1] < t1)
    print(t1, t2, 'No. earthquakes: ', sel_eq.sum(), 'No. of wells: ', sel_wells.sum())

    plt.figure(1)
    plt.cla()
    ax2 = plt.subplot(111)
    lon_0, lat_0 = .5*( dPar['xmin']+dPar['xmax']), .5*( dPar['ymin']+dPar['ymax'])
    m = Basemap(llcrnrlon = dPar['xmin'], urcrnrlon=dPar['xmax'],
                llcrnrlat = dPar['ymin'], urcrnrlat=dPar['ymax'],
                lon_0 = lon_0, lat_0 = lat_0,
                resolution = 'l',
                projection = dPar['projection'])

    m.drawcoastlines()
    aX_we, aY_we = m(injection_wells[2][sel_wells], injection_wells[3][sel_wells])
    m.plot(aX_we, aY_we, 'ro', ms = 2)
    aX_eq, aY_eq = m(seismic_activity[1][sel_eq], seismic_activity[2][sel_eq])
    m.plot(aX_eq, aY_eq, 'bo', ms = 2)
    m.drawparallels(np.arange(33, 38, 1), fmt = '%i', labels = [1, 0 , 0 , 0])
    m.drawmeridians(np.arange(-100, -92, 2), fmt = '%i', labels = [0, 0 , 0 , 1])
    print("Please click %i times"%( dPar['nClicks']))
    tCoord = plt.ginput( dPar['nClicks'])
    print("clicked", tCoord)
    plt.show()
    aLon = np.array(tCoord).T[0]
    aLat = np.array(tCoord).T[1]

"""
Part B
"""
#project into an equal-distance coorinate system
lon_0, lat_0 = .5*( dPar['xmin']+dPar['xmax']), .5*( dPar['ymin']+dPar['ymax'])
m = Basemap(llcrnrlon = dPar['xmin'], urcrnrlon=dPar['xmax'],
            llcrnrlat = dPar['ymin'], urcrnrlat=dPar['ymax'],
            projection=dPar['projection'], lon_0 = lon_0, lat_0 = lat_0)

"""
Part C
"""
#compute affected area
def area_poly(aX, aY):      #defining the function for the area of a polygon
    sumVert1 = np.dot(aX[0:-1], aY[1::])+aX[-1]*aY[0]
    sumVert2 = np.dot(aY[0:-1], aX[1::])+aY[-1]*aX[0]
    return 0.5*abs(sumVert1 - sumVert2)

aX, aY = (aX_we/1000, aY_we/1000) #converting from meters to kilometers
a_seis = area_poly(aX, aY)
print('Total area affected by seismicity: ', a_seis)
print('Fraction of area of OK: ', a_seis/(dPar['areaOK']))


