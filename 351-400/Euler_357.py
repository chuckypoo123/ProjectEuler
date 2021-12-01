# Find all primes up to 100,000,000
# Make a set with all numbers 1 less than the prime numbers.
# Check the prime factors (smaller than sqrt(num))

# Make set with all the numbers from 2 to 100,000,000
# Loop trough all numbers while doing the following
#   if number in set: (means number is prime)
#       remove all its multiples from the set
#       check if number - 1 has all its pairs of divisors summing up to primes

import timeit
from itertools import combinations

def prime_generating(num: int, primes: set) -> bool:
    # print(num)

    if (num % 4 == 0):
        return False

    sqrt = num ** 0.5
    for prime in primes:

        if prime > sqrt:
            continue

        if num % prime == 0:
            if num % (prime * prime) == 0:
                return False
            # print(num)
            # print(prime)
            # print()
            if (prime + num / prime) not in primes:
                return False

    return True

def base_fn(max_num: int):
    """
    numbers = {x for x in range(2, max_num + 2)} # We want to include max_num + 1 because we want to see if it is prime
    primes = set()
    pg_nums = []
    total = 0

    # print(numbers)
    # print()
    
    max_num_sqrt = int(max_num ** 0.5)
    for poss_prime in range (2, max_num_sqrt):
        if poss_prime in numbers: # meaning if it is a prime
            if prime_generating(poss_prime - 1, primes):
                    # pg_nums.append(poss_prime - 1)
                    total += poss_prime - 1

            for prime_mult in range(poss_prime, max_num + 2, poss_prime):
                if prime_mult in numbers:
                    numbers.remove(prime_mult)
                
            primes.add(poss_prime)

    # print(primes)

    for leftover_prime in numbers:
        primes.add(leftover_prime)

        if prime_generating(leftover_prime - 1, primes):
                # pg_nums.append(leftover_prime - 1)
                total += leftover_prime - 1
    """

    numbers = [True for x in range(max_num + 1)]
    primes = set()

    total = 0

    root_max_num = int(max_num ** 0.5)

    for i in range(2, root_max_num + 1):
        if numbers[i] == True:
            primes.add(i)
            for j in range(2 * i, max_num + 1, i):
                numbers[j] = False

            if prime_generating(i - 1, primes):
                total += i - 1

    for i in range(root_max_num + 1, max_num + 1):
        if numbers[i] == True:

            if prime_generating(i - 1, primes):
                total += i - 1
            
            primes.add(i)

    # print(primes)

    # print()
    # print(pg_nums)
    return total

def is_prime(num: int, primes):
    for prime in primes:
        if num == prime:
            return True
        if num % prime == 0:
            return False
    return True

def valid_combo(combo, max_num):
    prod = 1
    for element in combo:
        prod *= element
        if prod > max_num:
            return False

    return True

def fn(max_num: int):
    highest_prime = max_num //2
    primes = {x for x in range(2, highest_prime)} # We want to include max_num + 1 because we want to see if it is prime
    pg_nums = []
    total = 0 + 1 + 2 # 1 and 2 are not detected by the algorithm, so I add them manually

    # print(numbers)
    # print()
    highest_prime_sqrt = int(highest_prime ** 0.5) + 1
    for poss_prime in range (2, highest_prime_sqrt):
        if poss_prime in primes: # meaning if it is a prime

            for prime_mult in range(poss_prime*2, highest_prime, poss_prime):
                if prime_mult in primes:
                    primes.remove(prime_mult)

    print(primes)

    poss_pg = set()
    pg = set()

    for combo_length in range (2, len(primes) + 1):
        for combo in combinations(primes, combo_length):
            if (valid_combo(combo, max_num)):
                prod = 1
                for element in combo:
                    prod *= element
                
                poss_pg.add(prod)

                if is_prime(prod + 1, primes):
                    total += prod
                    pg.add(prod)

    print(poss_pg)
    print(pg)

    return total

if __name__ == "__main__":

    # Algorithm works, but takes way too long (1h and still not done)
    # Fast up to 1,000,000
    # print(fn(100000000))
    start = timeit.default_timer()
    print(base_fn(10000000))
    stop = timeit.default_timer()
    print("Time: " + str(stop - start) + "s")

    # print()

    # start = timeit.default_timer()
    # print(fn(1000))
    # stop = timeit.default_timer()
    # print("Time: " + str(stop - start) + "s")