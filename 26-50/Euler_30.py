# finding the sum of all the numbers for which the sum of each digit raised
# to the power of 5 is equal to the original number #

total = 0
for x in range(2, 1000000):
    listx = list(str(x))
    sum1 = 0
    for y in listx:
        sum1 += int(y)**5
        
    if sum1 == x:
        print(x)
        total += x
    
print("the total is", total)