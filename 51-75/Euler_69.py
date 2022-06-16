# finding n in range n<= 1,000,000 for which n/phi is highest #

# this means we want to maximize n and minimize phi(n)
# to do this, we should multiply all the smallest primes together until we reach our max value
# then we divide by the last prime we multiplied (to go back under the upper bound)
# having done this means the number is NOT coprime with all the primes used for the product
# this number is also as high as it can be

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