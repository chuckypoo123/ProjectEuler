# finding the number of different paths to get from one corner of a 20X20 grid
# to another while only being able to go right or down #

import math

y = 40

perm = math.factorial(y)/(math.factorial(y/2)**2)

print(perm)