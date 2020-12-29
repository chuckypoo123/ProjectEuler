# finding the smallest common multiplier of numbers from 1 to 20 #
var = 0
sum1 = 1

while sum1 != 0:
    var += 1
    sum1 = 0
    for x in range(2,21):
        y = var%x
        sum1 += y

print(var)

# this method takes a long time to run, the answer is 232 792 560
# finding all the primes to multiply together by hand is better
