import numpy as np

def decay(t,r):
	return np.exp(-r*t)


half_life = 5730

print(np.exp(1))
# fraction remaining after 10kyr
print(decay(10000, half_life))

# fraction remaining after 100kyr
print(decay(100000, half_life))

# fraction remaining after 1Mkyr
print(decay(1000000, half_life))