# finding the amount of circular primes below 1,000,000 #

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
    
counter = 2 # because program will ignore 2 and 5 because they are in 
            # cantprime (they are still circular numbers though)  
cantprime = [2, 4, 5, 6, 8, 0]
for x in range(2, 1000000):
    
    for y in cantprime:
        
        if str(y) in str(x):
            break
        
    else:

        if ifprime(x) is True:
            
            strx = str(x)
            
            for y in range(1, len(str(x))):
                
                modnum = int(strx[y:] + strx[:y])
                
                if ifprime(modnum) is False:                
                    break
            
            else:
                counter += 1
                
print(counter)