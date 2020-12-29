# finding the sum of all numbers below 1,000,000 which are palindromes in
# base 10 and base 2#

def ispalin(n):
    
    num1 = int(n)
    if num1 < 10:
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
    
sum1 = 0

for x in range(1, 1000000, 2):
    
    if ispalin(x) is True:
        
        binary = int(bin(x)[2:])
                     
        if ispalin(binary) is True:
            sum1 += x
            
print(sum1)