# finding the amount of Lychrel numbers under 10,000 #

def ispalin(n):
    
    if n < 10:
        return True
    
    strn = str(n)
    
    halfnum1 = list(strn[:len(strn)//2])
    halfnum1.reverse()
    if len(strn) % 2 == 0:
        halfnum2 = list(strn[len(strn)//2:])
    
    else:
        halfnum2 = list(strn[len(strn)//2 + 1:])
        
    if halfnum1 == halfnum2:
        return True
    
    else:
        return False
    
def revadd(n):
    
    global counter
    
    if n < 10:
        return n * 2
    
    revn = int(str(n)[::-1])
    
    sum1 = n + revn
    
    counter += 1
    
    return sum1

lychnum = 0

for x in range(1, 10001):
    
    counter = 0
    x = revadd(x)
    
    while ispalin(x) is False:
        
        x = revadd(x)
        
        if counter == 50:
            lychnum += 1
            break
        
print(lychnum)