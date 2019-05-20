import numpy as np
import matplotlib.pyplot as plt

data_file = 'midterm_dydx.txt'

mData = np.loadtxt(data_file).T
a_t, a_zt = mData[0], mData[1]



plt.figure(1)
ax1 = plt.subplot(111)
ax1.plot(a_t, a_zt, 'ko')
plt.show()
