#python2.7
"""
HW 4 #3

    -Modify the Newton's method function so that the following 
    criterion is met: f(x0[i+1]) - f(x0[i]) < eps

@author: scarletpasser
"""

def my_Newton( fct, df_dt, x0, tol = 1e-4, N = 20):
    """
    :param fct:     - find root of this fct. closes to x0
    :param dfct_dt: - derivatice of fct
    :param x0:      - initial guess of solution
    :param N:       - number of iterations, default = 20
    :param tol:     - tolerance, default = 1e-4
    :return: f_r0 - closest to x0
    """
    xn = float( x0)
    
    eps = 1e6   #define epsilon       
    x2 = xn + 1 #define new variable 
    
    i  = 0      
    
    while abs(fct( x2) - fct( xn)) < eps and i < N: # could also set fct. to ~0 to find root instead of min.
        
        x_next = xn - fct( xn)/df_dt( xn)
        print i, abs( fct( xn)), x_next
        xn = float( x_next)
        i += 1
    if abs( fct( xn)) > eps:# no solution found
        return None
    else:
        return float( x_next)
        



