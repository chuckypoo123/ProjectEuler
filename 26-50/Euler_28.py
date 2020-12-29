num = 1
sum1 = 1
period = 2

while period < 1001:
    
    for countperiod in range(4):
        num += period
        sum1 += num
        
    period += 2
    
print(sum1)