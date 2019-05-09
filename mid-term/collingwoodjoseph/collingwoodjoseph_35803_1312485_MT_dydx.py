# -*- coding: utf-8 -*-
"""
MIDTERM QUESTION 3
"""

import os
import numpy as np
import matplotlib.pyplot as plt

data_dir = 'C:\users\macn_000\Desktop\aapython'
mt_data = 'midterm_dydx.txt'
os.chdir(data_dir)

data = np.genfromtxt(mt_data, skip_header = 1).T
t, z = data[0],data[1]
delta_t = t[1::] - t[0:-1]

dz_dt = (z[0::]-z[0::])/(2*delta_t[0::])
d2z_dt2 = (z[0::]-2*z[0::]+z[0::])/(delta_t[0::])**2

plt.figure(1)
