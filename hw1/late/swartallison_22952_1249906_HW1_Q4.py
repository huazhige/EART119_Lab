# Allison Swart
# Astro/Earth 119 Homework 1
# April 14, 2019

#anaconda2/python2.7

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#              Problem 4
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# PART A


N = N0**(-time / tao)

# PART B

N0 = float( raw_input( 'What is the initial amount? ' ))
time = 10, 100, 100000
tao = 5730

N = N0**(-time / tao)

print 'NB = ', N

# PART C

N0 = float( raw_input( 'What is the initial amount? ' ))
time = float( raw_input( 'How much time is passing? ' ))
tao = float( raw_input( 'What is the half-life? ' ))

N = N0**(-time / tao)

print 'NC = ', N