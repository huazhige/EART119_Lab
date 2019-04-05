# Problem 2

import numpy as np

pi = np.pi

total = 0.
n = 50

for i in range(n+1):
    term = 8./((4.*i + 1.)*(4.*i + 3.))
    total = total + term
    print("Term:" + str(term))

print(total)
print(np.pi-total)

