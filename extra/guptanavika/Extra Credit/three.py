import numpy as np
import matplotlib.pyplot as plt
#3D plotting
from mpl_toolkits.mplot3d import axes3d
### my modules


def monteCarlo( f_xy, g_xy, xmin, xmax, ymin, ymax, n):
    """
        - integrate fct f_xy over potential complex domain omega described by g(x,y)
          --> g(x,y) has to defined so that pointes within domain follow:
              g(x,y) >= 0
        (1) randomly draw n points in x and y,
        (2) find points in domain g(x,y), which is embeded in a rectangle
            wiht Ar and bounded by (xmin, xmax, ymin, ymax)
        (3) compute mean function values of points inside of domain omega
        (4) compute area of domain omega from fraction of points and Ar
        (5) Int(f_xy dxdy) = f_mean*A_omega
    :param f_xy:  - function that should be integrated
    :param g_xy:  - function that defines integration domain
                    g >= 0
    g_xy is embeded in rectangle with:
    :param  - xmin, xmax, ymin, ymax
    :param n:  - number of random points in x and y, total no. = n**2

    :return: - float( ) - definite integral of f_xy
    """
    # create n random points in x and y
    a_xran = np.random.uniform( xmin, xmax, n)
    a_yran = np.random.uniform( ymin, ymax, n)
    ########### solve using for loop: A_om, f_mean###########
    f_fct_mean = 0
    num_inside = 0 # number of points with x,y; g(x,y) >= 0
    for i in range( n): # x loop
        for j in range( n): # y loop
            if g_xy( a_xran[i], a_yran[j]) >= 0:
                num_inside += 1
                f_fct_mean += f_xy( a_xran[i], a_yran[j])
    if (num_inside != 0):
        f_fct_mean /= num_inside
    # ############ vectorized version ###########
    # m_xran, m_yran = np.meshgrid( a_xran, a_yran)
    # sel = g_xy( m_xran, m_yran) >= 0
    # num_inside = sel.sum()
    # print( f_fct_mean)
    # f_fct_mean = np.mean( f_xy( m_xran[sel], m_yran[sel]))
    # print( f_fct_mean)

    # last two lines are the same for loop and vectorized solutions:
    # area of domain is approximate by q*Ar, where q is fraction of points in domain, and Ar is area of rectangle
    f_Aom       = num_inside/float(n**2) * (xmax-xmin)*(ymax-ymin)
    return f_Aom*f_fct_mean

def monteCarlo_vec( f_xy, g_xy, xmin, xmax, ymin, ymax, n):
    """
        - integrate fct f_xy over potential complex domain omega described by g(x,y)
          --> g(x,y) has to defined so that pointes within domain follow:
              g(x,y) >= 0
        (1) randomly draw n points in x and y,
        (2) find points in domain g(x,y), which is embeded in a rectangle
            wiht Ar and bounded by (xmin, xmax, ymin, ymax)
        (3) compute mean function values of points inside of domain omega
        (4) compute area of domain omega from fraction of points and Ar
        (5) Int(f_xy dxdy) = f_mean*A_omega
    :param f_xy:  - function that should be integrated
    :param g_xy:  - function that defines integration domain
                    g >= 0
    g_xy is embeded in rectangle with:
    :param  - xmin, xmax, ymin, ymax
    :param n:  - number of random points in x and y, total no. = n**2

    :return: - float( ) - definite integral of f_xy
    """
    # create n random points in x and y
    a_xran = np.random.uniform( xmin, xmax, n)
    a_yran = np.random.uniform( ymin, ymax, n)
    ############ vectorized version ###########
    m_xran, m_yran = np.meshgrid( a_xran, a_yran)
    sel = g_xy( m_xran, m_yran) >= 0
    num_inside = sel.sum()
    f_fct_mean = np.mean( f_xy( m_xran[sel], m_yran[sel]))
    # last two lines are the same for loop and vectorized solutions:
    # area of domain is approximate by q*Ar, where q is fraction of points in domain, and Ar is area of rectangle
    f_Aom       = num_inside/float(n**2) * (xmax-xmin)*(ymax-ymin)
    return f_Aom*f_fct_mean

# x= np.linspace (0, 2, N)
# y= np.linspace (0, 1.5, N)

# def f(x, y):
#     return ((x**2)+(y**2))^(1/2)

# def w(x, y):
#     return x*(y**2)



# -------------------------

def fct2_xy( x, y):
    return np.sqrt(x**2 + y**2)

def fct_xy( x, y):
    return x*y**2

def fct_gxy( x, y):
    """
    - rectangular domain
     return: -1 for points outside
    """
    f_retVal = -1
    if x >= 0 and x >= 2 and y >= 0 and y <= 1.5:
        f_retVal = 1
    return f_retVal

#================================================
#           parameters 
#================================================
xmin, xmax = 0, 2
ymin, ymax = 0, 1.5 

a_x = np.linspace( -4, 4, 100)
a_y = np.linspace( -4, 4, 100)


#================================================
#          compute integral 
#================================================

n=100

done = monteCarlo(fct_xy, fct_gxy, xmin, xmax, ymin, ymax, n)

print "integral:"
print done


done2 = monteCarlo(fct2_xy, fct_gxy, xmin, xmax, ymin, ymax, n)
print "integral:"
print done2
#================================================
#            plotting
#================================================
m_X, m_Y = np.meshgrid( a_x, a_y)
m_Z      = fct_xy( m_X, m_Y)
m_Z      = fct2_xy( m_X, m_Y)

fig1 = plt.figure(1, figsize=(10,10))    
ax = axes3d.Axes3D( fig1)
plot1 = ax.plot_surface( m_X, m_Y, m_Z, cmap = plt.cm.coolwarm_r, linewidth=0, shade = True)
cbar = plt.colorbar( plot1, shrink = .5, aspect = 20)
#-----------------labels and legends-------------------------------------
cbar.set_label( 'f(x,y)')
ax.set_xlabel( 'x')
ax.set_ylabel( 'y')
ax.set_zlabel( 'z = f(x,y)')
plt.show()
