# -*- coding: utf-8 -*-
#python2.7

# =============================================================================
#                              Problem 5.
# =============================================================================

import numpy as np
import matplotlib.pyplot as plt
import opt_utils as opt

# =============================================================================
#                           Define variables
# =============================================================================

t = np.linspace(0.000000, 1.000000, 500)
dt = 0.002004 # Time incremement

# I'm not sure how to reverse engineer the function z(t) given its values.
# I'm assuming that we're supposed to do this in python and not by hand.