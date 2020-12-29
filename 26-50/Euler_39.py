# finding the value p for which there are the biggest amount of solution of
# pythag (integers)
# (consider p as the perimeter and the solution as the sides. You are trying
# to find the perimeter for which there are the most solutions) #

maxsol = 0
for p in range(3, 1000):
    sols = 0
    c = p - 2
    b = 1
    a = 1
    
    while a < p//3:
        
        if c**2 == a**2 + b**2:
            sols += 1
            c -= 1
            b += 1
    
        elif c**2 > a**2 + b**2:
            c -= 1
            b += 1
        
        elif c**2 < a**2 + b**2:
            a += 1
            b = a
            c = p - (a + b)
            
    if sols > maxsol:
        maxsol = sols
        pmaxsol = p
        
print(maxsol, pmaxsol)