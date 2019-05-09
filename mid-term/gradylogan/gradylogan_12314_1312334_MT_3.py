# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

#===============================================================================
# Loading in the data
#=============================================================================== 
pfile = 'midterm_dydx.txt'
pData = np.loadtxt( pfile, comments = '#').T
t, z = pData[0], pData[1]

#===============================================================================
# Derivations
#===============================================================================
#z(t) vs time 
t_step = t[1] - t[0]
#z'(t) vs time
vel = (z[2::] - z[0:-2])/(2*t_step)
#z''(t) vs time
acc = (vel[2::] - vel[0:-2])/(2*t_step)

#since this is using the central difference method, the first and last variables
#are shortened by one each 'derivative', so I have to shorten the bounds by one each time

#===============================================================================
# Plots
#===============================================================================   
plt.figure()
pvt = plt.subplot(311)
pvt.plot(t,z, 'r-')
pvt.set_xlabel('Time(s)'), pvt.set_ylabel('z(t) (m)')
vvt = plt.subplot(312)
vvt.plot(t[1:-1], vel, 'r-')
vvt.set_xlabel('Time(s)'), vvt.set_ylabel('v(t)')
avt = plt.subplot(313)
avt.plot(t[2:-2], acc, 'r-')
avt.set_ylim(-20,0)
avt.set_xlabel('Time(s)'), avt.set_ylabel('a(t) (m/s^2)')

plt.savefig('Midterm_Prob3_Plot')
