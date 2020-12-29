# finding the smallest integer x that has the same digits as 2*x, 3*x,
# 4*x, 5*x, 6*x #

var = 1
mult = 2

while mult < 6:
    
    list1 = list(str(var))
    list1.sort()
    
    prod = var * mult
    listx = list(str(prod))
    listx.sort()
    
    if listx == list1:
        mult += 1
        
    else:
        mult = 2
        var += 1
        
print(var)