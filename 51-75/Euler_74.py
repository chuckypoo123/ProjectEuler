# SOLVED
# Min time: 1.65 sec

import math
import timeit

def factorial_digits_sum(num: int):
    
    total = 0

    while num != 0:
        total += math.factorial(num % 10)
        num //= 10

    return total

def main():

    loop_lengths = [0 for i in range(1000000)]

    loop_lengths[169] = 3
    loop_lengths[363601] = 3
    loop_lengths[1454] = 3

    loop_lengths[871] = 2
    loop_lengths[45361] = 2
    loop_lengths[872] = 2
    loop_lengths[45362] = 2

    loop_lengths[145] = 1

    loop_lengths[1] = 1
    loop_lengths[2] = 1

    count = 0

    for i in range(3, 1000000): # 1! and 2! are 1 and 2. They are a loop of 1

        # If loop length of this number is already found, skip it
        if loop_lengths[i] != 0:
            continue

        sequence = [i]

        while True:
            fds = factorial_digits_sum(i)

            if fds < 1000000:

                if fds == i:
                    loop_lengths[fds] = 1
                    break

                if loop_lengths[fds] != 0:
                    break

            i = fds
            sequence.append(i)

        seqlen = len(sequence)
        # print(sequence)
        for i in range(seqlen):

            if sequence[i] >= 1000000:
                continue

            loop_length = seqlen + loop_lengths[fds] - i
            loop_lengths[sequence[i]] = seqlen + loop_lengths[fds] - i

            if loop_length == 60:
                count += 1

    return count
if __name__ == "__main__":
    start = timeit.default_timer()
    print(main())
    print("Time taken: " + str(timeit.default_timer() - start))