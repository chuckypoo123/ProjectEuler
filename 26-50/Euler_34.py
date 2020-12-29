# finding the sum of the all the numbers for which the sum of the factorial 
# of their digits is equal to the number #

import math

total = 0
for x in range(3, 7*math.factorial(9)): # 7*9! is the upper bound because 8*9!
                                        # gives only a 7 digit number
    
    num = list(str(x))
    facsum = 0
    
    for y in num:
        facdig = math.factorial(int(y))
        facsum += facdig
        
    if facsum == x:
        total += x
        
print(total)        