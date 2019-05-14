

def area_polygon(x,y):
	sum = 0
	for i in range(len(x)):
		sum += x[i]*y[(i+1)%len(y)] - y[i]*x[(i+1)%len(x)]
	return .5 * sum



