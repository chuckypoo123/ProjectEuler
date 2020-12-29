# finding the fisrt odd composite number that cannot be expressed as
# the sum of a prime and of the double of a square #

notfound = True
primes = {2, 3, 5, 7}
rang = 10

while notfound is True:
    
    upbound = rang * 10
    for x in range(rang, upbound):
        primes.add(x)
    
    a = 2    
    while a < (upbound ** 0.5) + 1:
        if a in primes:
            for b in range(a*2, upbound, a):
                if b in primes:
                    primes.remove(b)
                    
        a += 1
    
    for x in range(rang, upbound):
        if x % 2 == 0:
            continue
        
        elif x in primes:
            continue
        
        else:
            for y in primes:
                
                if y < x:
                
                    result = ((x - y) / 2) ** 0.5
                
                    if result.is_integer() is True:
                        break
                
            else:
                print(x)
                notfound = False
                break
               
    rang *= 10