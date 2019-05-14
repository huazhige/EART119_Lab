"Python 3.6"
"Problem 4"
"Radioactive decay"

import numpy as np
import math


def leftovers(ini_amount,t_elapsed,t_halflife):
	if type(ini_amount) == str:
		N = math.exp(-t_elapsed/t_halflife)
		print("final amount: " + str(N) + " * " + str(ini_amount))
	else:
		N = ini_amount*math.exp(-t_elapsed/t_halflife)
		print("final amount: " + str(N))

leftovers("C", 10E3, 5740)

leftovers("C", 10E4, 5740)

leftovers("C", 10E6, 5740)
