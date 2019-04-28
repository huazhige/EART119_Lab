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

#print (area(x,y))

#def area(*x, *y):

sum1=0
sum2=0

for i in range(len(x)-1):
	sum1 += x[i]*y[i+1]

sum1 = sum1 + x[len(x)-1]*y[0]


for j in range(len(x)-1):
	sum2 = sum2 + y[j]*x[j+1]

sum2 = sum2 + y[len(x)-	1]*x[0]

sum=abs(sum1-sum2)
sum = sum/2

print sum


