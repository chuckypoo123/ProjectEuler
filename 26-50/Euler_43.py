# finding the sum of all pandigital numbers that have d2d3d4 dividable by 2,
# d3d4d5 divisible by 3, d4d5d6 divisible by 5, d5d6d7 divisible by 7,
# d6d7d8 divisible by 11, d7d8d9 divisible by 13 & d8d9d10 divisible by 17 #

from itertools import permutations

total = 0

perm = list(permutations(list(range(10))))

for x in perm:
    str1 = ""
    for y in x:
        str1 += str(y)
        
    if int(str1[3]) % 2 != 0:
        continue
    
    elif int(str1[2:5]) % 3 != 0:
        continue
    
    elif int(str1[3:6]) % 5 != 0:
        continue     
    
    elif int(str1[4:7]) % 7 != 0:
        continue
    
    elif int(str1[5:8]) % 11 != 0:
        continue
    
    elif int(str1[6:9]) % 13 != 0:
        continue
    
    elif int(str1[7:10]) % 17 != 0:
        continue
    
    else:
        total += int(str1)
        
print(total)