# finding the highest sum of the digits of a number out of all the numbers
# that can be expressed as a^b where both a and b < 100

hidigsum = 0
abmax = 0

for a in range(2, 100):
    for b in range(2, 100):
        
        sum1 = 0
        
        ab = a**b
        
        abstr = str(ab)
        
        for x in abstr:
            sum1 += int(x)
            
        if sum1 > hidigsum:
            hidigsum = sum1
            abmax = ab
            
print(hidigsum, abmax)