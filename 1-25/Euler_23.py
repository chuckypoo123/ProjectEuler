# finding the sum of all numbers who cannot be expressed as the sum of
# abundant numbers

sum1 = 0
abnum = []

for x in range(1,28124):
  
# this first part checks if x is abundant

    div = [1]    
    var = 2
    
    while var < x :
        
        if x % var == 0:
            div.append(var)
            
        var += 1
    
    if sum(div) > x:
        abnum.append(x)
        
# this second part check if x is the sum of 2 abundant numbers

    for y in abnum:
        
        z = x - y
        
        if z in abnum:
            break
    else:
        sum1 += x
    
print(sum1)

# this works, but takes about 2 minutes to run