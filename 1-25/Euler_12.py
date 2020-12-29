# finding the first triangular number with over 500 divisors #

triang = 0
add = 1
numdiv = 0

while numdiv <= 500:
    
    triang += add
    add += 1
    numdiv = 0
    var = 2
    y = triang**0.5 #having y as a variable makes it so the comp doesn't have to 
                    #recalculate the root every time it does the comparison    
    while var <= y :
        if triang%var == 0:
            numdiv += 1
        var += 1
    
    numdiv *= 2
    
    if var**2 == triang:
        numdiv -= 1
    
print(triang)

# this would work, but takes way too much time. 