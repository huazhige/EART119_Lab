import math
r = 12.6

a = 1.5

b = 0



while math.sqrt(a*a+b*b)<=(r*2):
	b+= 0.00001

if math.sqrt(a*a+b*b)>(r*2):
	b = b - 0.00001



# this is the closest I think I can get to using a while loop, accurate up to 4 decimals
print(b)

#this is the closest possible, using some algebra
x = (r*2)**2 - a**2
print(math.sqrt(x))