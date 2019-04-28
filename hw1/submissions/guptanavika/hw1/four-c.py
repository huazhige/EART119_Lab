import math
def halfLife(time, half):
	test=10*math.exp(-(time/half))
	act=test/10
	return act

print("elapsed time?")
time = input()

print("half-life?")
half = input()

print (halfLife(half, time))

