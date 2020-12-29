# finding 2 pentagonal numbers for which their sum and difference are also
# triangular numbers (answer is the difference between those 2 numbers) #

pentaset = set()
pentaindex = 1
notfound = True

while notfound is True:

    newpenta = int(pentaindex*(3*pentaindex - 1)/2)
    
    for x in pentaset:
        dif1 = newpenta - x
        
        if dif1 in pentaset:
            dif2 = abs(x - dif1)
            
            if dif2 in pentaset:
                print(dif2)
                notfound = False
                break
        
    pentaset.add(newpenta)
    pentaindex += 1