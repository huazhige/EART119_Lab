# -*- coding: utf-8 -*-

x     = (1,3,4,3.5,2)
y     = (1,1,2,5,4)
total = 0
for i in range(0,5):
    term = .5*((x[i-1]*y[i])-(y[i-1]*x[i]))
    total = total + term
    print 'term:', term
print 'Final area =', total





# These are a bunch of mini tests I did to try out for loops and ranges
"""collection = ['hey', 5, 'd']
for i in collection:
    print i
#prints out list of all items in 'collection'
    for x in range (0, 3):
#prints out values with the string from 0 to 2
   
    print "We're on time %d" % (x)
#produces values 1 to 3
    y = x+1
    print y"""
