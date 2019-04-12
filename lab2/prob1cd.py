# Problem 2 for lab2

# Import modules
import numpy as np

if __name__ == "__main__":

    # Define f and g function
    # Constants
    c = 1.1
    t0 = 2.5
    A = 5.
    x_max = 10.
    x_min = -10.
    N = 1000
    eps = 0.1
    # Initialize the time series
    time = np.linspace(x_min, x_max, num=N)
    f = c*(time-t0)**2.
    g = A*time+t0
    distance = np.abs(f-g)
    
    for idis in distance:
       if (idis < eps):
         print("Distance: " + str(idis))
    

