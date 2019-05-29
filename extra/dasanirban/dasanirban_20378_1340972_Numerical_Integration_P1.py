import math
def midpointMethod(n):
  a=0.0 #lower bound
  b=1.0 #upper bound
  d=(b-a)/n #delta x
  f=a+(d/2) #first position
  m=[] #list of midpoints
  m.append(f)
  for i in range(n-1): #append all midpoints to list
    f+=d
    m.append(f)
  c=[] #list of f(midpoints)
  for i in m: #append all f(midpoints) to list
    c.append((3*(i**2)*(math.exp(i**2))))
  return d*(sum(c)) #return integral approximation
print midpointMethod(100)