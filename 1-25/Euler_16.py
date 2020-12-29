# finding the sum of the digits of the result of 2^1000 #

list1 = [int(x) for x in str(2**1000)]

print(sum(list1))

# could be done in 1 line like this:
# print(sum([int(x) for x in str(2**1000)]))