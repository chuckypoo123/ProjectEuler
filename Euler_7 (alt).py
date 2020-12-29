# finding the 10,001th prime #

## This is the sieve of erastothenes
upbound = 200000 #try to pick a high enough bound to have your nth prime in #
primes = list(range(2,upbound))

i = 2
while i <= int(upbound**0.5):
    
    if i in primes:
        
        for j in range(i*2, upbound, i):
            
            if j in primes:
                primes.remove(j)
        
    i += 1

print(primes[10000])