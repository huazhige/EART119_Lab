#python2.7
"""
    use the dot product to compute mean and std of a data matrix m_Data

    - use numpy.random to create a 10x12 matrix of random numbers drawn from
      a normal distribution with mu and std

"""
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

#===================================================================================
#                                params
#===================================================================================
# mean and standard deviation
iWells = 10
iMeas  = 12

a_mu_syn   = np.random.randint( 1, 40, iWells)*1.1 # mean pressure in MPa
a_std_syn  = np.random.randint( 1, 20, iWells)*.1  # stdev in MPa
