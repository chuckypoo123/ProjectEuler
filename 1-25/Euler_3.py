# finding the biggest prime multiple of num #
num = 600851475143
var = 2

while num != 1 :
    while num % var != 0 :
        var += 1

    print(var)

    num = num/var