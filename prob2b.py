# Problem 2

import numpy as np

total = 0.
n = 10

for i in range(n+1):
    term = 8./( (4.*i+1.)*(4.*i+3.) )
    total = total + term

    print("term:" + str(term))

print(total)
print(np.pi-total)
