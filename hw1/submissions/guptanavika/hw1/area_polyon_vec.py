import math
import sys
import array
import numpy as np

print("How many vertecies?")

#numV=input()
num = input()

x= np.empty((num))
y= np.empty((num))

#x[0]=3;

#

#x = array


for i in range(num):
	print ("x corrdinate "+str(i+1)+":")
	x[i]=input()

	print ("y corrdinate "+str(i+1)+":")
	y[i]=input()

print(x)
print(y)

x1 = np.empty((num))
y1 = np.empty((num))

for j in range(num-1):
	x1[j+1]=x[j]
	y1[j+1]	=y[j]

x1[0]=x[num-1]
y1[0]=y[num-1]

#print (x)
#print(x1)

#print (y)
#print (y1)

sum1=np.dot(x,y1)
#print(sum1)
sum2=np.dot(x1,y)
#print(sum2)

sum=abs(sum1-sum2)
sum = sum/2

print sum	


