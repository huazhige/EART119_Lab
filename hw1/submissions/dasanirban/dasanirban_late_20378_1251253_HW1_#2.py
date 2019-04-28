#part i
def area_polygon(x,y): #where x and y are lists of the x and y coordinates, going clockwise
  a=[]
  for i in range(len(x)-1):
    a.append((x[i])*(y[i+1]))
  a.append(x[len(x)-1]*y[0])
  b=[]
  for i in range(len(y)-1):
    b.append((y[i])*(x[i+1]))
  b.append(y[len(x)-1]*x[0])
  return .5*(abs(sum(a)-sum(b)))

print area_polygon([0,1,1,0],[1,1,0,0])

#part ii
import numpy
def area_polygon_vec(x,y): #I did not implement this one properly
  y=numpy.roll(y,1)
  a=[]
  for i in range(len(x)):
    a.append(x[i]*y[i])
  return sum(a)

print area_polygon_vec([0,1,1,0],[1,1,0,0])
