import re

def txt_to_list_of_columns(filename: str):
    file = open(filename, "r").read().strip()
    matrix = [[int(y) for y in re.split(",", x)] for x in re.split("\n", file)]
    matrix = list(map(list, zip(*matrix)))
    return matrix

if __name__ == "__main__":
    cols = txt_to_list_of_columns("Euler_81_matrix.txt")