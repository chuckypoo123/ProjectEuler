# SOLVED
# Min time: 0.33sec

import timeit
import sympy

def main():
    # PRIMES_UP_TO = 1000000
    # start = timeit.default_timer()
    # primes = [True for x in range(PRIMES_UP_TO)]
    # primes[0] = False
    # primes[1] = False

    # for i in range(int(PRIMES_UP_TO**0.5)):
    #         if primes[i]:
    #             for j in range(i*2, len(primes), i):
    #                 primes[j] = False

    # print(f"Primes found {timeit.default_timer() -start} sec")

    prime_counter = 0
    corner_list = [1]

    i = 2
    increment = 2 # square side length = increment + 1

    # for x in range(5):
    while True:
        try:
            i += increment - 1
            corner_list.append(i)
            if sympy.isprime(i):
                prime_counter += 1

            for k in range(3):
                i += increment
                corner_list.append(i)
                if sympy.isprime(i):
                    prime_counter += 1
        except:
            print(i)
            print(prime_counter)
            print(len(corner_list))
            return

        if 10 * prime_counter < len(corner_list):
            return [prime_counter, len(corner_list), increment + 1]

        i += 1

        increment += 2

    # return [prime_counter, len(corner_list), increment + 1, corner_list]

if __name__ == "__main__":
    start = timeit.default_timer()
    print(main())
    print(f"Time taken: {timeit.default_timer() - start} sec")