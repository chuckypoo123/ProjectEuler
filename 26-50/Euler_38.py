# finding the biggest pandigital number that can be made from concatenated 
# products

digits = list(range(1, 10))
biggest = 0
for x in range(10000):
    
    fac = 1
    concat = ""
    while len(concat) < 9:
         concat += str(x * fac)
         fac += 1
         
    if len(concat) > 9:
        continue
    
    for x in digits:
        strdig = str(x)
        
        if strdig not in concat:
            break
        
    else:
        numconcat = int(concat)
        if numconcat > biggest:
            biggest = numconcat
            
print(biggest)