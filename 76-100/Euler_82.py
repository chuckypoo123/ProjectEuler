"""
Given an nxn matrix, find a path starting from any cell in the left column and ending in any cell
in the right column that will minimize the sum of the cells encountered.
You can only move up, right, and left.

Ex:
 131   673  _234_ _103_ _018_
_201_ _096_ _342_  965   150
 630   803   746   422   111
 537   699   497   121   956
 805   732   524   037   331
"""

"""
Logic: Because we cannot move back, we can try to reduce the matric column by column.
We can do this by finding the minimal way to reach each cell in a given column.
For the example above
"""
import re

def reduce_col(col1: list[int], col2: list[int]):
    new_col2 = col2.copy()
    # Finding the optimal way (min_sum) to reach row i in col2
    for i in range(len(col2)):

        # Initial min_sum is the result of going directly to the right 
        min_sum = col1[i]
        # print(f"Starting min_sum for row {i}: {min_sum}")

        # When the starting row is above the end row (j < i)
        for j in range(i):
            path_sum = col1[j]

            for k in range(j, i):
                path_sum += col2[k]

            if path_sum < min_sum:
                # print(f"min_sum reduced: starting at: {col1[j]}")
                # print(path_sum)
                # print(j)
                # print(col2[j])
                min_sum = path_sum

        # When the start row is below the end row (j > i)
        for j in range (i + 1, len(col2)):
            path_sum = col1[j]

            for k in range(i + 1, j + 1):
                path_sum += col2[k]

            if path_sum < min_sum:
                # print(f"min_sum reduced: starting at: {col1[j]}")
                min_sum = path_sum

        new_col2[i] += min_sum
    return new_col2

def reduce_last_col(col1: list[int], col2: list[int]):
    min_sum = col1[0] + col2[0]
    for i in range(1, len(col1)):
        poss_min_sum = col1[i] + col2[i]
        if poss_min_sum < min_sum:
            min_sum = poss_min_sum
    return min_sum

def txt_to_list_of_columns(filename: str):
    file = open(filename, "r").read().strip()
    matrix = [[int(y) for y in re.split(",", x)] for x in re.split("\n", file)]
    matrix = list(map(list, zip(*matrix)))
    return matrix

def solve82():
    matrix = txt_to_list_of_columns("Euler_82_matrix.txt")
    for i in range(78):
        matrix[i+1] = reduce_col(matrix[i], matrix[i+1])
    min_sum = reduce_last_col(matrix[78], matrix[79])
    print(min_sum)

def tests():
    matrix = [[131, 201, 630, 537, 805], [673, 96, 803, 699, 732], [234, 342, 746, 497, 524], [103, 965, 422, 121, 37], [18, 150, 111, 956, 331]]
    matrix = list(map(list, zip(*matrix)))
    print(matrix)
    # # reduce_col(matrix[0], matrix[1])
    # for i in range(3):
    #     matrix[i+1] = reduce_col(matrix[i], matrix[i+1])
    #     print(matrix)
    # print(reduce_last_col(matrix[3], matrix[4]))
    # print(txt_to_list_of_columns("Euler_82_matrix.txt"))

if __name__ == "__main__":
    # tests()
    solve82()

"""
Ex:
 131   673  _234_ _103_ _018_
_201_ _096_ _342_  965   150
 630   803   746   422   111
 537   699   497   121   956
 805   732   524   037   331
"""