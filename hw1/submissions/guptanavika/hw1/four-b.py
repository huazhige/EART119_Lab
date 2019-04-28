import math

def halfLifeOfC(time):
	temp=10*math.exp(-(time/5730))
	done=temp/10
	return done

print(halfLifeOfC(10000))
print(halfLifeOfC(100000))
print(halfLifeOfC(1000000))