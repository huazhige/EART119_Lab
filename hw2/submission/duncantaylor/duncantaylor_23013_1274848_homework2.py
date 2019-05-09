
xmin, xmax  = -180+1e-4, 180

ymin, ymax  = -90+1e-4, 90

print(xmin, xmax)
print(ymin, ymax)

#coordintes	
	tCoord = plt.ginput( nPoints)
	X = np.array( tCoord).T[0]
	Y = np.array( tCoord).T[1]

aYr  = np.genfromtxt( "seism_OK.txt", skip_header = 1, usecols=(0), delimiter='-', dtype = int)

mLoc = np.genfromtxt( "seism_OK.txt", skip_header = 1, usecols=(2,1), delimiter=',', dtype = float).T
# get magnitude information and also latitude and longitude
mLoc = np.genfromtxt( "seism_OK.txt", skip_header = 1, usecols=(2,1,4), delimiter=',', dtype = float).T

sort_id = aYr.argsort()

aYr = aYr[sort_id]
mLoc= mLoc.T[sort_id].T

for it in np.unique( aYr):
    sel_eq = it == aYr
    print( 'current year', it, '#no. of events: ', sel_eq.sum())



