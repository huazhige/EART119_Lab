"""
Lili Callahan
Homework #4

"""

#   Problem 3
"""
This problem modifies the function for Newton's method.

"""

def my_Newton( fct, df_dt, x0, tol = 1e-6, N = 20):
    """
    :param fct:     - find root of this fct. closes to x0
    :param dfct_dt: - derivatice of fct
    :param x0:      - initial guess of solution
    :param N:       - number of iterations, default = 20
    :param tol:     - tolerance, default = 1e-4
    :return: f_r0 - closest to x0
    """
    xn = float( x0)
    x2 = xn + 1
    i  = 0
    while abs( fct( x2) - fct(xn)) > tol and i < N:
        x_next = xn - fct( xn)/df_dt( xn)
        print i, abs( fct( xn)), x_next
        xn = float( x_next)
        i += 1
    if abs( fct( xn)) > tol:
        return None
    else:
        return float( x_next)

    
