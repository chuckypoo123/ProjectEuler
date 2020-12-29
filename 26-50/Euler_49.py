# finding the concatenation of the 3 4-digit primes that are permutations of
# one another and that are also the result of a series (x(n) + y = 
# x(n + 1)) #

from itertools import permutations

primes = set(range(2, 10000))
i = 2
upbound = int(10000 ** 0.5) + 1

while i < upbound:
    
    if i in primes:
        for j in range(i*2, 10000, i):
            if j in primes:
                primes.remove(j)
            
    i += 1
    
for x in range(1000):
    if x in primes:
        primes.remove(x)
        
for x in primes:
    
    priperm = []
    perm = set(permutations(str(x)))
    
    for y in perm:
        strnum = ""
        for z in y:
            strnum += str(z)
            
        intnum = int(strnum)
    
        if intnum in primes:
            priperm.append(intnum)
            
    if len(priperm) >= 3:
        priperm.sort()
        
        for y in priperm:
            for z in priperm:
                if y == z:
                    continue
                
                middle = int((y + z) / 2)
                
                if middle == 4817:
                    continue
                
                if middle in priperm:
                    seq = [y, z, middle]
                    seq.sort()
                    concat = ""
                    for a in seq:
                        concat += str(a)
                    
                    print(seq)
                    print(concat)
                    print(seq[1] - seq[0], seq[2] - seq[1])
                    break
                
            else:
                continue
            
            break
        
        else:
            continue
            
            break
        
    else:
        continue
    
    break
        
        