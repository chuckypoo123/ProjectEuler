# finding the sum of the only 11 primes that are truncatable from the right
# and the left #

def isprime(n):
    if n == 1:
        return False
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
    
truncpri = set()
primes = {2, 3, 5, 7}
canthave = {2, 4, 6, 8, 0, 5}
num = 11

while len(truncpri) < 11:
    for x in primes:
        if num % x == 0:
            num += 1
            break
    else:
        strnum = str(num)
        for x in canthave:
            if str(x) in strnum[1:]:
                num += 1
                break
            
        else:    
            primes.add(num)
            for y in range(1, len(strnum)):
                modnum = strnum[:y]
                
                if isprime(int(modnum)) is False:
                    break
                
                modnum = strnum[y:]
                
                if isprime(int(modnum)) is False:
                    break
                
            else:
                truncpri.add(num)
                print(num)

print(sum(truncpri))