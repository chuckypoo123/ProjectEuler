# finding the longest Collatz chain for a number under 1,000,000 
# Collatz = n/2 or 3n+1 repeatedly until you get to 1 #

var = 500000
longchain = []

while var < 1000000 :
    
    mod = var
    chain = []
    
    while mod != 1:
        
        chain.append(mod)
        
        if mod % 2 == 0:
            mod /= 2
            
        else: 
            mod *= 3
            mod += 1
    
    if len(chain) > len(longchain):
        longchain = chain
    
    var += 1
    
print(longchain[0])
print(len(longchain))