# -*- coding: utf-8 -*-
"""
    -Problem 3:
        Taking first and second derivatives using CD of data given
"""
import numpy as np
import matplotlib.pyplot as plt
import os
#================
data_dir = 'data'
data_file = 'midterm_dydx.txt'
os.chdir(data_dir)
data_ld = np.genfromtxt(data_file, skip_header=1).T

a_t = data_ld[0]
a_z = data_ld[1]
z_max = max(a_z)
mz_id = np.arange(data_ld[0].shape[0])[data_ld[1] == z_max] 
t_maxz  = a_t[mz_id[0]]

dt = .1
t0 = z_max*np.exp(t_maxz**2) #finding initial velocity to use in fct

def fct(t):
    return t0*np.exp(-t**2)
def vfct(t):
    return t0*(-t**2)*np.exp((-t**2)-1)

dzdt_CD = (fct(a_t+dt) - fct(a_t-dt))/(2*dt) 
dz2d2t_CD = (vfct(a_t+dt) - vfct(a_t-dt))/(2*dt)

