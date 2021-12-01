# Finding the number of irreductible fractions greater than 1/3, but smaller than 1/2
# with the denominator 

# SOLVED
# Min time: 5.89sec
# Past min times: 11.95sec, 14sec, 22sec, 89sec

# Procedure
# Count number greater than 1/3 (f13)
# Count number greater than 1/2 (f12)
# f13 - f12 - 1 (this 1 is to count 1/2)

import timeit
import math

def primes_until(max_num: int) -> set:

    numbers = [True for x in range(max_num + 1)]
    primes = set()

    root_max_num = int(max_num ** 0.5)

    for i in range(2, root_max_num + 1):
        if numbers[i] == True:
            primes.add(i)
            for j in range(2 * i, max_num + 1, i):
                numbers[j] = False

    for i in range(root_max_num + 1, max_num + 1):
        if numbers[i] == True:
            primes.add(i)

    return primes

def factorize(num, primes):
    factors = set()

    for prime in primes:
        if num % prime == 0:
            factors.add(prime)

    return factors

def fractions_greater_than(num_base_fract: int, denom_base_fract: int, max_denom: int) -> int: # 89sec runtime
    primes = primes_until(max_denom)
    total = 0

    for denom in range(2, max_denom + 1):
        denom_factors = factorize(denom, primes)
        for num in range(1, denom):
            if (num * denom_base_fract > denom * num_base_fract)\
                and (factorize(num, denom_factors) == set()):
                total += 1
                # print(num)
                # print(denom)
                # print()

    return total

def fract_betw_13_12(): # 11.95sec runtime

    total = 0
    max_num = 12000
    half_max_num = max_num // 2
    root_max_num = int(max_num ** 0.5)

    numbers = [True for x in range(half_max_num + 1)]
    primes = set()

    for denom in range(2, root_max_num + 1):
        denom_factors = factorize(denom, primes)
        for num in range(denom//3 + 1, (denom + 1) // 2):
            """Last argument above -1 (because we don't want to include 1/2,
            but +1 because ranges don't include the last value"""
            if (factorize(num, denom_factors) == set()):
                total += 1

        if numbers[denom] == True:
            primes.add(denom)
            for j in range(2 * denom, half_max_num + 1, denom):
                numbers[j] = False

    for denom in range(root_max_num + 1, half_max_num + 1):
        denom_factors = factorize(denom, primes)
        for num in range(denom//3 + 1, (denom + 1) // 2):
            """Last argument above -1 (because we don't want to include 1/2,
            but +1 because ranges don't include the last value"""
            if (factorize(num, denom_factors) == set()):
                total += 1

            if numbers[denom] == True:
                primes.add(denom)

    for denom in range(half_max_num + 1, max_num + 1):
        denom_factors = factorize(denom, primes)
        for num in range(denom//3 + 1, (denom + 1) // 2):
            """Last argument above -1 (because we don't want to include 1/2,
            but +1 because ranges don't include the last value"""
            if (factorize(num, denom_factors) == set()):
                total += 1

    return total

def gcd_frac(): # 5.89sec runtime

    total = 0

    max_num = 12000
    min_frac_num = 1
    min_frac_denom = 3
    max_frac_num = 1
    max_frac_denom = 2

    for denom in range(2, max_num + 1):
        for num in range(denom // min_frac_denom + 1, (denom + 1) // max_frac_denom):
            if math.gcd(num, denom) == 1:
                total += 1

    return total

if __name__ == "__main__":
    # start = timeit.default_timer()
    # f13 = fractions_greater_than(1, 3, 12000)
    # f12 = fractions_greater_than(1, 2, 12000)
    # stop = timeit.default_timer()
    # print(f13)
    # print(f12)
    # print(f13 - f12 - 1)
    start = timeit.default_timer()
    print(gcd_frac())
    stop = timeit.default_timer()
    print("Time: " + str(stop - start) + "s")

    # print("Done")