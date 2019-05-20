# -*- coding: utf-8 -*-

"""

Q5


"""

import numpy as np
import matplotlib.pyplot as plt
import os

data = np.loadtxt('HW4_vertTraj.txt').T

t  = data[0]
zt = data[1]

dt  = t[2::] - t[0:-2]

dfdt_CD = (zt[2::] - zt[0:-2])/(2*dt)

df2dt2_CD = (zt[2::] - 2*zt[1:-1] + zt[0:-2])/(dt**2)

#df2d2z = (f_z[2::] - 2*f_z[1:-1] + f_z[0:-2])/(delta_z[1::])**2

plt.figure()
#plt.title('Projectile', loc = 'center')

plt.subplot(311)
plt.plot(t,zt)
plt.ylabel('Position (m)')

plt.subplot(312)
plt.plot(t[0:-2], dfdt_CD)
plt.ylabel('Velocity (m/s)')

plt.subplot(313)
plt.plot(t[0:-2], df2dt2_CD)
#plt.ylim(0,-.005)
plt.ylabel('Accelaration (m/s^2)')
plt.xlabel('Time (s)')

plt.subplots_adjust(hspace = 0.5)


os.chdir( r'X:\ASTRO 119\Astro119\Homework 4')
plt.savefig( 'Projectile')
plt.show()