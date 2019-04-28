import numpy as np

def area_polygon_vec(x,y):
	return .5 * np.linalg.norm(np.cross(x,y))