# finding the sum of products for which the multiplicand/multiplier/product
# expression is pandigital 1-9

from itertools import permutations
setpan = set()

perm = list(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9]))

for x in perm: 
    # when 2 digits * 3 digits = 4 digits
    mult1 = int(str(x[0]) + str(x[1]))
    mult2 = int(str(x[2]) + str(x[3]) + str(x[4]))
    prod = int(str(x[5]) + str(x[6]) + str(x[7]) + str(x[8]))
    
    if mult1 * mult2 == prod :
        print(mult1, mult2, prod)
        setpan.add(prod)
    
    # when 1 digit * 4 digits = 4 digits
    mult1 = x[0]
    mult2 = int(str(x[1]) + str(x[2]) + str(x[3]) + str(x[4]))
    prod = int(str(x[5]) + str(x[6]) + str(x[7]) + str(x[8]))
    
    if mult1 * mult2 == prod :
        print(mult1, mult2, prod)
        setpan.add(prod)
        
print(setpan, sum(setpan), sep = "\n")