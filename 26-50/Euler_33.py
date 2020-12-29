# finding the reduced denominator of the fraction obtained by mutliplying the
# 4  2-digit-over-2 digit fractions that can be wrongly reduced and still
# work (e.g. 49/98) (30/50 is a trivial example) #

wrongred = []
reddenomprod = 1
for a in range(10, 100):
    for b in range(10, 100):
        
        if a >= b:
            continue
        
        a1 = int(str(a)[0])
        a2 = int(str(a)[1])
        b1 = int(str(b)[0])
        b2 = int(str(b)[1])
        realquot = a/b
        
        if b2 == 0:
            continue
        
        
        if a1 == b1:
            if a2/b2 == realquot:
                wrongred.append(str(a) + "/" + str(b))
                reddenomprod *= (b2/a2)
        
        elif a1 == b2:
            if a2/b1 == realquot:
                wrongred.append(str(a) + "/" + str(b))
                reddenomprod *= (b1/a2)
                
        if a2 == b1:
            if a1/b2 == realquot:
                wrongred.append(str(a) + "/" + str(b))
                reddenomprod *= (b2/a1)
        
        elif a2 == b2:
            if a1/b1 == realquot:
                wrongred.append(str(a) + "/" + str(b))
                reddenomprod *= (b1/a1)
                
print(wrongred)
print(reddenomprod)

