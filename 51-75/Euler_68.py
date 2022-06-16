# https://projecteuler.net/problem=68
# Magic 5-gon ring

# 1. Reduce data set:
#   - Must be 16 digits, so 10 cannot appear in center ring
#   - Sum of digits from 1 to 10 = 55. Sum of lines = x, total sum of lines = 5x
#       total sum = 5x = (sum from 1 to 10) + (sum of digits in ring)
#       Therefore, sume of digits in ring, must be a multiple of 5.
#       Using num_mod5(), I have found that there are only 26 ways to choose 5 numbers from 1 to 9 s.t. they are divisible by 5.
#   Data set reduced!

# 2. Write an algorithm that builds the magic 5-gon from the 5 middle digits:
#   A. Find the sum of each branch (55 + (sum of middle 5))
#   B. For each outer number, find the pair(s) of middle numbers that make outer + inner1 + inner2 = branch_sum
#       If no such pair exist for any outer number, it means a magic 5-gon cannot be created from these inner and outer numbers
#       This condition rules out all but 2 options for inner and outer numbers!
#   C. Build a list where each index corresponds to the index of an inner number (a 5-item list, where all items are iniialized to 0)
#       1. Using the outer numbers that have only 1 possible pair, start filling the list.
#       2. Traverse the list of pairs and remove all the pairs that contain a number that must appear twice already.
#       3. 

# Solved!

from itertools import combinations

def num_mod5():
    comb = combinations([x for x in range(1, 10)], 5)

    mod5 = 0

    for i in list(comb):
        if sum(i) % 5 == 0:
            mod5 += 1
            print(f"Numbers: {i}, Sum: {sum(i)}")

    return mod5

def get_inner_nums():
    comb = combinations([x for x in range(1, 10)], 5)

    mod5 = []

    for i in list(comb):
        if sum(i) % 5 == 0:
            mod5.append(i)

    return mod5

def build_5gon(inner_nums):
    inner_nums = list(inner_nums)
    outer_nums = [x for x in range(1, 11) if x not in inner_nums]
    branch_sum = (sum(inner_nums) + 55) // 5

    # print(branch_sum)
    print(inner_nums)
    print(outer_nums)
    # print()

    outer_num_pairs = []

    for num in outer_nums:
        temp_sum = branch_sum - num
        # print(f"Outer num: {num}, temp sum: {temp_sum}")
        combs = combinations(inner_nums, 2)
        pairs = [comb for comb in combs if sum(comb) == temp_sum]
        if len(pairs) == 0:
            outer_num_pairs = None
            break
        outer_num_pairs.append(pairs)

    return outer_num_pairs

if __name__ == "__main__":
    mod5 = get_inner_nums()
    for inner_nums in mod5:
        print(build_5gon(inner_nums))
        print()