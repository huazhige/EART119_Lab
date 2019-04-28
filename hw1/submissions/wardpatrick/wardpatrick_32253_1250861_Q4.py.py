# -*- coding: utf-8 -*-

"""

Q4

"""

#================================
#            part a
#================================

import math

n0  = 10
t   = 100
tao = 5730

def amount(n0, t, tao):
    N = n0*math.e**(-t/tao)
    return (N)
print ('Part a)', amount(n0, t, tao))


#================================
#            part b
#================================
t1 = [10000, 100000, 1000000]

for i in range (len(t1)):
    N = n0*math.e**(-1*t1[i]/tao)
    
    print ('Part b)', N)
### there's practically nothing left after 100k years

    
    
#================================
#            part c
#================================

n0 = int(input('Initial Amount:'))
t = int(input('Elapsed Time:'))
tao = int(input ('Halflife:'))


N = n0*math.e**(-1*t/tao)

print ('Part C)', N)
