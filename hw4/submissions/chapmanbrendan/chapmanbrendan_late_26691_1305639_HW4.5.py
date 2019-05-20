# -*- coding: utf-8 -*-
"""
Created on Sun May  5 23:49:22 2019

@author: brend
"""

import numpy as np
from matplotlib import pyplot as plt
import os
from mpl_toolkits.mplot3d import Axes3D
import glob
import yt
from yt.config import ytcfg
#========================================================================================================================
""" Question 5
Plot Accelerations 
"""
#========================================================================================================================




path = ("HW4_vertTraj.txt")

my_fns = glob.glob(path+"/Orbit/orbit_hdf5_chk_00[0-9][0-9]")
my_fns.sort()
fields = [" t[s]", "z(t) [m]"]

indices = dd["particle_index"].astype("int")
print (indices)

ts = yt.DatasetSeries(my_fns)
# suppress_logging=True cuts down on a lot of noise
trajs = ts.particle_trajectories(indices, fields=fields, suppress_logging=True)
print (trajs["particle_position_x"])
print (trajs["particle_position_x"].shape)