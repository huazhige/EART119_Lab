"""
Astr/Earth-119, Homework-1, problem 2
Finding the area of a polygon using vectors
"""
import numpy as np
#================================================
# (x,y) coordinates =====================================
x_crdnts1 = np.array([1, 3, 4, 3.5, 2])
y_crdnts1 = np.array([4, 1, 1, 2, 5])
x_crdnts2 = np.array([2, 1, 3, 4, 3.5])
y_crdnts2 = np.array([1, 1, 2, 5, 4])
Ints_x = (0, 1, 2, 3, 4)
Ints_y = (1, 2, 3, 4, 0)

#cCalculation =============================
N = x_crdnts1 * y_crdnts1
O = np.sum(N)
print(O)

M = x_crdnts2 * y_crdnts2
P = np.sum(M)
print(P)



U = np.abs((O-P)/2)
print(U)
