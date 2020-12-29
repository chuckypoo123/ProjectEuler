# finding the biggest period for 1/d for d < 1000 #

longest = 0

for d in range(1, 1000):
    
    period = False
    listrem = []
    rem = 1
    
    while period is False :
        
        rem %= d
        
        if rem in listrem:
            period = True
        
        else:
            listrem.append(rem)
            
        rem *= 10
    
    x = len(listrem)
    
    if x > longest:
        longest = x
        longdecnum = d

print(longdecnum, longest, sep = ' with a period of ')