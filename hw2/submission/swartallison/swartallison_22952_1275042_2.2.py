# Allison Swart
# Astro/Earth 119 Homework #2
# April 23, 2019

#anaconda2/python2.7

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#              Problem 2
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# PART A

tCoordinate = plt.ginput(2010)
xCoordinate = np.array( tCoordinate).T[0]
yCoordinate = np.array( tCoordinate).T[1]
plt.show()

# PART B

M = Basemap( width = 8000000, height = 7000000, resolution = 'l', 
             projection = 'aea')