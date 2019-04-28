"Python 3.6"
"Problem 3"
"Maximum length of rectangle's side"

import numpy as np

r=12.6 #radius of circle
a=1.5  #known side of rectangle
b=0    #unknown side of rectangle

while (a*b < np.pi*r**2):
	b += 1                        #while loop adds 1 to b after stopping, therefore b-1 is correct answer
print("maximum b: " + str(b-1))

