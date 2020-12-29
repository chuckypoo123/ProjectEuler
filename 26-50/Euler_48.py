#finding the last 10 digits of the sum of a**a for a from 1 to 1000 #

sum1 = 0

for a in range(1, 1001):
    sum1 += a**a
    
print(str(sum1)[-10:])