# finding the amount of time the fraction approximation of root 2 has a
# numerator with more digits than the denominator #

from fractions import Fraction

def contfrac(n):
    
    if n == 1:
        res = 2 + 1 / 2
        res = Fraction(res)
        return res

    res = 2 + 1 / contfrac(n - 1)
    
    res = Fraction(str(res))

    return res   

counter = 0

for x in range(1, 1001):
    x = str(contfrac(x) - 1)
    listx = [y for y in x.split("/")]
    if len(listx[0]) > len(listx[1]):
        counter += 1

print(counter)