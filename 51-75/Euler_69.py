# finding n in range n<= 1,000,000 for which n/phi is highest #

n = 1
primes = list(range(2, 100)) # 100 as upper bound was chosen randomly
i= 2

while i <= 100**0.5: # this gets all the primes below 100
    if i in primes:
        for j in range(i*2, 100, i):
            if j in primes:
                primes.remove(j)
        
    i += 1

for x in range(len(primes)): # this makes n increase using primes
    
    n *= primes[x]
    
    if n > 1000000: # this keeps n under 1,000,000
        n /= primes[x]
        print(primes[x])
        break
    
print(int(n))