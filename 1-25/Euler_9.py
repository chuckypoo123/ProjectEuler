# finding the product of the only Pythagoren triplet whose sum is 1000 #

notfound = True
c = 998
b = 1
a = 1

while notfound is True:
    
    if c**2 == a**2 + b**2:
        notfound = False
    
    elif c**2 > a**2 + b**2:
        c -= 1
        b += 1
        
    else:
        a += 1
        b = a
        c = 1000 - a - b

print(a, b, c)
print(a*b*c)