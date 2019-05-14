import numpy as np

# input variables
x = [1, 3, 4, 3.5, 2]
y = [1, 1, 2, 5, 4]

def area(x,y):
    
    x2 = list(x)
    y2 = list(y)
    
    x2.append(x[0])
    y2.append(y[0])
    
    del x2[0]
    del y2[0]
    
    return 0.5 * (np.dot(x, y2) - np.dot(x2, y))
print("The Area is: " + str(area(x,y)))