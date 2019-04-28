
#N= N0exp(-t/t)
#Where Nis the quantity
#of the substance, t
#is the half-life, and
#t is the elapsed time since a reference time t0. 

import math

def halfLife( init, time, half):
	sum=init*math.exp(-(time/half))
	return sum

def halflife(time, half):
	test=10*math.exp(-(time/half))
	act=test/10
	return act

