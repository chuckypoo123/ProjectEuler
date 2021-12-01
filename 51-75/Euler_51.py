# finding the smallest prime which, by replacing part of the number (not
# necessarily adjacent digits, is part of an 8 prime value family

# SOLVED
# Min time: 0.52s

import timeit

def num_as_list(num: int) -> list:

    numlist = [set() for x in range(10)]
    index = len(str(num)) - 1
    while num != 0:
        numlist[num % 10].add(index)
        index -= 1
        num //= 10

    return numlist

def main():

    FAMILY_LEN = 8

    primes = [True for x in range(10)]
    primes[0] = False
    primes[1] = False

    for i in range(len(primes)):
            if primes[i]:
                for j in range(i*2, len(primes), i):
                    primes[j] = False

    for order in range(2, 8):

        # print(primes)
        primes.extend([True for x in range(9*len(primes))])

        for i in range(len(primes)):
            if primes[i]:
                for j in range(i*2, len(primes), i):
                    primes[j] = False

        # print(len(primes))

        for i in range(len(primes)//10, len(primes)):

            if not primes[i]:
                continue

            # print(i)
            numlist = num_as_list(i)
            # print(numlist)
            for j in range(len(numlist)):

                if not len(numlist[j]):
                    continue

                count_not_prime = 0
                prime_family = []
                for permutation in range(10):
                    numstr = str(i)

                    for index in numlist[j]:
                        if index == 0 and permutation == 0:
                            continue
                        numstr = numstr[:index] + str(permutation) + numstr[index + 1:]

                    numperm = int(numstr)

                    if not primes[numperm]:
                        count_not_prime += 1

                        if count_not_prime > 10 - FAMILY_LEN:
                            break
                    else:
                        # print(numperm)
                        prime_family.append(numperm)

                else:
                    return prime_family
                    # print("First number in family" + str(i))
    else:
        print("No number found")
        return 0             

# found all primes
if __name__ == "__main__":
    start = timeit.default_timer()
    print(main())

    # print(len(str(101)))

    # set1 = set()
    # print(len(set1))

    # string1 = "abcdefg"
    # string2 = string1[:6] + "A" + string1[7:]
    # print(string2)
    stop = timeit.default_timer()
    # print(primes)
    print("Time: " + str(stop - start) + "s")