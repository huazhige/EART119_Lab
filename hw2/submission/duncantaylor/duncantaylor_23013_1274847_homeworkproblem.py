import numpy as np
import matplotlib.pyplot as pyplot

#load data
wellData = np.loadtxt("injWell_OK.txt").T
seisData = np.loadtxt("seism_OK.txt").T

wellData.transpose()
seisData.transpose()

# DecYear = YR + (MO-1)/12 + (DY-1)/365.25+ HR/(365.25*24) + MN/(365.25*24*60) + SC/(365.25*24*3600)
#rate of earthquakes 
k= 200
N= number of earthquakes
#cumulative number of earthquakes
(use np.cumsum( np.ones( 'injWell_OK')))
(use np.cumsum( np.ones( 'seism_OK')))

print(use np.cumsum( np.ones( 'injWell_OK.txt")))
print(use np.cumsum( np.ones( "seism_OK.txt")))
#subplot earhquake rates

plt.subplot('seism_OK')
plt.plot( k, N)
plt.xlabel('time')
plt.ylabel( 'earthquake rates')

#sublot cumulative number

plt.subplot('injWell_OK')
plt.plot( k, N)
plt.xlabel('time')
plt.ylabel( 'cumulative number')
#variables
dT= 6 months
#for loop 2015-2018
np.logical_and(2015,2018)

for x in xrange(2015,2018):
	












