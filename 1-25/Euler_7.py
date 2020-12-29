# finding the 10,001th prime #
primes = [2]
var = 3
    
while len(primes) < 10001: # number is the nth prime you're trying to find
        
    i = 0
    while i < len(primes):
        
        for x in primes:
            
            y = var%x
            
            if y == 0:
                var += 1
                i = 0 # When var has % of 0, var is a multiple of x.
                      # i is rest to 0 to make sure new var goes through the
                      # whole list of primes.
            else:
                i += 1
                pass # If % != to 0, var is not a multiple of x.
                     # i += 1 makes sure var will be compared to each x in
                     # primes only once

    primes.append(var)
    var += 1
    
print(primes[10000]) # number is the (n-1)th prime you're trying to find