# -*- coding: utf-8 -*-
import numpy as np

#============================================================================
#                             Parameters
#============================================================================
x_points = [1, 3, 4, 3.5, 2]
y_points = [1, 1, 2, 5, 4]

#============================================================================
#                             For Loop
#============================================================================

def area_polygon(x_points, y_points):
    term1 = []
    x_len = len(x_points) - 1
    
    for n in range(0, x_len):
        elem = x_points[n] * y_points[n+1]
        term1.append(elem)
    term1.append(x_points[x_len]*y_points[0])

    term2 = []
    for n in range(0,x_len):
        elem = y_points[n] * x_points[n+1]
        term2.append(elem)
    term2.append(y_points[x_len]*x_points[0])
    
    term1sum = np.sum(term1)
    term2sum = np.sum(term2)
    
    A = 0.5 * (term1sum - term2sum)
    
    return A

area_polygon(x_points, y_points)


#============================================================================
#                            vectorized
#============================================================================

def area_polygon_vec(x_i, y_i):
    #inputs: column vector of vertex xvalues, yvalues
    
    #create vectors going from initial point to each other vertex
    vectors = []
    for n in range(1, len(x_i)):
        x = x_i[0] - x_i[n]
        y = y_i[0] - y_i[n]
        vectors.append([x,y])
    print(vectors)
    
    #take cross product of adjacent vectors to determine area
    #of triangular section between
    a_triangles = []
    for m in range(0, len(vectors)-1):
        a_triangle = np.abs(0.5 * np.linalg.norm(np.cross(vectors[m], vectors[m+1])))
        print(a_triangle)
        a_triangles.append(a_triangle)
    
    #sum area of triangles to obtain area of polygon    
    A = np.sum(a_triangles)
    return A

        
area_polygon_vec(x_points, y_points)
