"Python 3.6"
"Problem #2"
"Area of an irregular polygon"



import numpy as np

#x and y are coordinates of 5 vertices of irregular polygon
x = [1,3,4,3.5,2]
y = [1,1,2,5,4]
A = 0               #Area

for n in range(5):
	A = A + 0.5*((x[n-1]*y[n]) - (x[n]*y[n-1]))  #note, for n = 0, x[-1] = x[4]
print("area: " + str(A))
