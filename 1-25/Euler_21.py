# finding the sum of amicable numbers under 10,000 #

amic = []

for var in range(2, 10000):
    
    if var in amic:
        continue
    
    x = 2
    y = var**0.5
    sumdiv1 = 1
    
    while x < y:
        if var % x == 0:
            sumdiv1 += x
            sumdiv1 += var/x
        
        x += 1
    
    if x**2 == var:
        sumdiv1 -= x
    
    if sumdiv1 < 0 or sumdiv1>= 10000:
        continue

#----------------------------------
    x = 2
    y = sumdiv1**0.5
    sumdiv2 = 1
    
    while x < y:
        if sumdiv1 % x == 0:
            sumdiv2 += x
            sumdiv2 += sumdiv1/x
        
        x += 1
    
    if x**2 == sumdiv1:
        sumdiv2 -= x
    
    if sumdiv1 >= 10000:
        continue
        
    if sumdiv2 == var and sumdiv1 != var:
        amic.append(var)
        amic.append(sumdiv1)
    
print(amic, sum(amic), sep = "\n")