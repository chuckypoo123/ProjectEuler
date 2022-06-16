# how many numbers of n-digits are nth power numbers
import timeit

start = timeit.default_timer()
total = 0
for i in range(1, 10):
    num = i
    power = 1

    while len(str(num)) == power:
        print(i, power)
        total += 1
        num *= i
        power += 1

print()
print(total)
print(f"Time taken: {timeit.default_timer() - start}s")