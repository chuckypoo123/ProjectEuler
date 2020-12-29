# finding the amount of number combinations n choose r for 1 <= n <= 100
# where the result is greater than 1,000,000 #

import math

counter = 0

for n in range(1, 101):
    for r in range(1, n):
        nchor = math.factorial(n) / (math.factorial(r)\
            * math.factorial(n-r))
            
        if nchor > 1000000:
            counter += 1
            
print(counter)