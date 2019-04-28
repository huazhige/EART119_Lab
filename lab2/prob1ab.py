# Problem 1 for lab2

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

    # Calculate distance.
    for t in time:
        # Define functions
        f = c*(t-t0)**2.
        g = A*t+t0
        distance = np.abs(f-g)
        if (distance < 0.1):
            print("Distance: " + str(distance))
            print("Location of Satellite A: " + str(f))
            print("Location of Satellite B: " + str(g))
            print("The coresspoint happens at: " + str(t))
    

