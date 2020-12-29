# finding the difference between the square of the sum and the sum of the 
# squares of numbers from 1 to 100 #
ans = 0

for x in range(1, 101):
    y = x**2
    ans -= y
    
sum1 = 0
for x in range(1, 101):
    sum1 += x
    
sum1 **= 2
ans += sum1
    
print(ans)