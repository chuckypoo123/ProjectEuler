# finding the sum of the digits in 100! #

import math

res = [int(x) for x in str(math.factorial(100))]

print(sum(res))