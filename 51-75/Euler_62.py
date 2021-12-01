# Finding the smallest cubic number that can permute in 4 other cubes
# Ex: 41063625 (345^3) and 56623104 (384^3) and 66430125 (405^3)

# SOLVED
# Min time: 2.2sec

# Procedure
# Store cubes as a list as follows [list_of_digits, num1, num2, num3, num4, num5]
# list_of_digits has 10 entries. The value is the number of times the index appears in the number.
import timeit

def num_as_list(num):
    # digits    0  1  2  3  4  5  6  7  8  9
    num_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    while num != 0:
        num_list[num % 10] += 1
        num //= 10
    return num_list

def fn(num_permutations, num = 1): # If num is input, the algorithm will start looking at cubes from this number
    permutations_list = []
    cube_len = 0
    length_for_solve = num_permutations + 1
    while True:
        cube = num * num * num
        digits = num_as_list(cube)

        for i in range(len(permutations_list)):
            if digits == permutations_list[i][0]:
                permutations_list[i].append(num)
                if len(permutations_list[i]) == length_for_solve:
                    return permutations_list[i]
                break
        else: # If permutation not found, add it to the list
            permutations_list.append([digits, num])

        num += 1

# list1 = [1, 2, 3, 4]
# list2 = [1, 2, 3, 4]
# print(list1 == list2)

# print(num_as_list(345))

if __name__ == "__main__":

    start = timeit.default_timer()
    list1 = fn(5, 345)
    stop = timeit.default_timer()
    print(list1)
    print(list1[1] * list1[1] * list1[1])
    print("Time: " + str(stop - start) + "s")