# Finding the number of reduced fractions (fractions where the numerator and denominator are
# coprime) that exist when the denominator <= 1,000,000

# Approach: 
# 1. For each number i in the range, find the number of numbers < i, that are coprime to i.
#   - We do not need to find out what they are, we only have to find how many
#   - To do so, we can follow a simple algorithm found below.
# 2. Sum all these numbers

# Finding the number of coprimes
# What we know:
# There are i - 1 numbers that have the chance to be coprime
# All prime factors are not coprimes. Same applies for all multiples of the prime factors
# (provided they are still < i). This should be all the non-coprimes.
# We need to be careful of not overcounting the non-coprimes
#   - For a given prime factor p, there are floor(i/p) multiples of p less than i.
#   - For 2 given prime factors p1 and p2, removing all the multiples of p1 and p2 from the set of
#       i - 1 possible coprimes, will remove the multiples of p1*p2 twice, these must be readded
#   - For 3 given prime factors p1, p2, p3, readding all multiples of p1*p2, p1*p3, and p2*p3,
#       will readd the multiples of p1*p2*p3 3 times (2 times more than necessary), these must be
#       removed
#   - This can keep going on until we reach all prime factors mutliplied together (primes squared 
#       should count only once I think)
#       - Odd loops should be subtracted and even should be added

# Notes:
#   - Algorithm works for 8, but takes way too long for 1,000,000
#       Let's try making find_prime_factors faster
#   - For a given prime p, there are p - 1 coprime numbers

from itertools import combinations, count
from timeit import default_timer

# First, a simple algorithm to find prime factors
def find_prime_factors(n, primes):
    prime_factors = set()

    for prime in primes:
        while n % prime == 0:
            prime_factors.add(prime)
            n //= prime

    # This is a slow way of doing it, looking at all possible numbers
    # counter = 2
    # while n != 1:
    #     if n % counter == 0:
    #         prime_factors.add(counter)
    #         n //= counter
    #     else:
    #         counter += 1

    return prime_factors

# Counting the coprimes of n 
def count_coprimes(n, primes):
    start = default_timer()

    prime_factors = find_prime_factors(n, primes)

    pf_time = default_timer() - start

    if len(prime_factors) == 0: # If a number is prime all numbers below it a coprimes
        primes.add(n)
        return n - 1

    coprimes = n

    for loop in range(1, len(prime_factors) + 1):
        for combination in combinations(prime_factors, loop):
            product = 1
            for i in range(loop): # Loop is the same number as the length of the cobination tuple
                product *= combination[i]

            num_mult = n // product
            if loop & 1 == 1: # If loop is odd
                coprimes -= num_mult
            else:
                coprimes += num_mult

    loop_time = default_timer() - start - pf_time

    if n > 10000 and (n  & 0b111111111) == 0:
        print(f"{n} - Prime factors time: {pf_time}, Loop time: {loop_time}")

    return coprimes

# Finally, adding all numbers of coprimes together.
def counting_fractions(n):
    sum = 0
    primes = set()
    for i in range (2, n + 1): # Denominator of fraction is between 2 and n inclusively
        sum += count_coprimes(i, primes)

    return sum

if __name__ == "__main__":
# Testing find_prime_factors
    # print(find_prime_factors(8, {2}))
    # print(find_prime_factors(15, {2, 3, 5, 7, 11, 13}))
    # print(find_prime_factors(36, {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}))

# Testing count_coprimes
    # print(count_coprimes(30, {2, 3, 5, 7, 11, 13, 17, 19, 23, 29}))

# Test coutin_fractions
    print(counting_fractions(1000000))