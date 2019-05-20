# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import opt_utils as opt_utils
#===============================================================================
# Loading in the data
#=============================================================================== 
pfile = 'HW4_vertTraj.txt'
pData = np.loadtxt( pfile, comments = '#').T
t, z = pData[0], pData[1]

#===============================================================================
# Derivations
#=============================================================================== 
t_step = t[1] - t[0]
vel = (z[2::] - z[0:-2])/(2*t_step)
acc = (vel[2::] - vel[0:-2])/(2*t_step)

#===============================================================================
# Plots
#===============================================================================   
plt.figure()
pvt = plt.subplot(311)
pvt.plot(t,z, 'r-')
pvt.set_xlabel('Time'), pvt.set_ylabel('Position')
vvt = plt.subplot(312)
vvt.plot(t[1:-1], vel, 'r-')
vvt.set_xlabel('Time'), vvt.set_ylabel('Velocity')
avt = plt.subplot(313)
avt.plot(t[2:-2], acc, 'r-')
avt.set_xlabel('Time'), avt.set_ylabel('Acceleration')
plt.show()
