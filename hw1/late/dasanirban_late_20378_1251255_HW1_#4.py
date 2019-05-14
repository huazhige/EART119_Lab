#part a
import math
def radioactiveDecay(time,halfLife,initalAmount=None):
  if initalAmount==None:
    return 100*math.exp(-time/halfLife)
  else:
    return initalAmount*math.exp(-time/halfLife)

print radioactiveDecay(1,2,3)

#part b
i=10000
while i<=1000000:
  print str(radioactiveDecay(i,5730))+" percent remains after "+str(i)+" years."
  i*=10

#part c
m=float(raw_input("What is the half-life of the material? "))
i=float(raw_input("How many years to start at? "))
while i<=1000000:
  print str(radioactiveDecay(i,m))+" percent remains after "+str(i)+" years."
  i*=10
