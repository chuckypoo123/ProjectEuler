# finding the sum of all the primes under 2,000,000 #

upbound = 2000000
primes = set(range(2,upbound))

i = 2
while i <= int(upbound**0.5):
    
    if i in primes:
        
        for j in range(i*2, upbound, i):
            
            if j in primes:
                primes.remove(j)
        
    i += 1

print(sum(primes))