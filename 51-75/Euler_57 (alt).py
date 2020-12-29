# finding the amount of time the fraction approximation of root 2 has a
# numerator with more digits than the denominator #

from fractions import Fraction

contfrac = 2 + 1/2

counter = 0

for x in range(2, 1001):
    
    contfrac = 2 + 1 / contfrac
    contfrac = Fraction(str(contfrac))
    
    listfrac = [x for x in str(contfrac - 1).split("/")]
    
    if len(listfrac[0]) > len(listfrac[1]):
        counter += 1
        
print(counter)