import math
import numpy as np
import matplotlib.pyplot as plt


data  = np.genfromtxt('midterm_dydx.txt', dtype=float).T


z=data[0]
t=data[1]

# print z

plt.figure()

plt.plot(z, t, 'b-')



vel=np.empty(len(data[0]))
t2=np.empty(len(data[0]))


for i in range(len(data[0])-1):
	vel[i]=(z[i+1]-z[i])
	t2[i]=(t[i+1]-t[i])

plt.figure()

plt.plot(vel, t2, 'r-')

plt.show()

acc=np.empty(len(data[0]))
t3=np.empty(len(data[0]))


for i in range(len(data[0])-1):
	acc[i]=(vel[i+1]-vel[i])
	t3[i]=(t2[i+1]-t2[i])



plt.figure()

plt.plot(acc, t3, 'g-')

plt.show()