# finding the first 4 consecutive integers with 4 distinct prime factors
# each #

num = 2
possdiv = 2
counter = 0
fourdivs = []

while counter < 4:
    
    divisors = set()    
    numcopy = num
    possdiv = 2
    
    while numcopy != 1 :
        while numcopy % possdiv != 0:
            possdiv += 1
            
        divisors.add(possdiv)
        numcopy = numcopy/possdiv
        
    if len(divisors) == 4:
        counter += 1
        fourdivs.append(num)
        
    else: 
        counter = 0
        fourdivs.clear()
        
    num += 1
    
print(fourdivs)

# works but is a little long: ans is 134,043