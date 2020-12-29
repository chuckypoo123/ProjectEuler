# finding the number under 1,000,000 that can be expressed as the longest
# possible sum of consecutive primes #

primeset = set(range(2, 1000000))

i = 2
upbound = int(1000000 ** 0.5) + 1

while i < upbound:
        if i in primeset:
            for j in range(i*2, 1000000, i):
                if j in primeset:
                    primeset.remove(j)
                
        i += 1
                
primes = list(primeset)
primes.sort()

x = 0
des = False
maxlencon = 0
maxcon = 0

while x < len(primes) - 2:
    
    sum1 = 0
    y = x
    
    while sum1 < 1000000:
        sum1 += primes[y]
        y += 1
    
    notprime = True
    
    while notprime is True:
        
        if y - x + 1 < maxlencon:
            break
        
        y -= 1
        
        if y < 0: break
        
        if sum1 in primes:
            lencon = y - x + 1
            if lencon > maxlencon:
                maxlencon = lencon
                maxcon = sum1
                
            notprime = False
        
        else: 
            sum1 -= primes[y]
        
    x += 1
    
print(maxcon, maxlencon)