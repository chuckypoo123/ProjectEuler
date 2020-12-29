# Find the product of the coefficients, a and b, for the quadratic expression
# n**2 + an + b that produces the maximum number of primes for consecutive
# values of n, starting with n=0 #

# Intial function

def func(a, b, n):
    x = n**2 + a*n + b
    return x

# List of primes under 1000 (possible values for b)

primes = list(range(2, 1000))
k = int(1000**0.5)
i = 2
for i in range(k):
    if i in primes:
        for j in range(i*2, 1000, i):
            if j in primes:
                primes.remove(j)
                
# Finding if a number is prime

def ifprime(n):
    x = int(n**0.5) + 1
    possdiv = list(range(2, x))
    i = 2
    while i <= x**0.5:
        if i in possdiv:
            for j in range(i*2, x, i):
                if j in possdiv:
                    possdiv.remove(j)
        i += 1
    
    for y in range(len(possdiv)):
        if n % possdiv[y] == 0:
            return False
            break
    else:
        return True

# Finding the values of a and b

maxn = 0
for b in primes:
    for a in range(-999, 1000):
        n = 1
        restart = False
        while restart is False:
            if func(a, b, n) <= 0:
                restart = True
            
            elif ifprime(func(a, b, n)) is True:
                n += 1
            else:
                restart = True
                
        if n > maxn:
            maxn = n
            maxa = a
            maxb = b
        
print("The maximum number of consecutive primes is: ", maxn, sep = "")
print("It was achieved using ", maxa, " for a, and ", maxb, " for b",\
      sep = "")
print("The product of a and b is ", maxa*maxb, sep = "")