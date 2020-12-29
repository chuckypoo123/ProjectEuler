# finding the biggest pandigital prime

from itertools import permutations

digits = "987654321"

notfound = True

while notfound is True:
    
    x = int(int(digits)**0.5) + 1
    possdiv = list(range(2, x))
    i = 2
    while i <= x**0.5:
        if i in possdiv:
            for j in range(i*2, x, i):
                if j in possdiv:
                    possdiv.remove(j)
        i += 1
        
    pan = list(permutations(list(digits)))
    
    for x in pan:
        
        str1 = ""
        for y in x:
            str1 += str(y)
        
        int1 = int(str1)
        
        if possdiv[-1] > int1**0.5:
            possdiv.pop()
        
        for z in range(len(possdiv)):
            if int1 % possdiv[z] == 0:
                break
            
        else:
            print(int1)
            notfound = False
            break
    
    else:
        digits = digits[1:]