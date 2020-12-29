# finding the biggest reduced fraction smaller than 3/7 for all
# the fractions n / d for n < d and for d <= 1,000,000 #

from math import gcd

def getkey(val, dict1):
    for key, value in dict1.items():
        if val == value:
            return key
        
max1 = 3 / 7
lval = 0
lfracstr = ""

for d in range(1, 1000001):
    
    n = 3 * d //7
    
    m = gcd(n, d)
    
    n //= m
    d //= m
    
    val = n / d        
    
    if lval < val < max1:
            lval = val
            frac = str(n) + "/" + str(d)
            lfracstr = frac

print(lfracstr, lval)