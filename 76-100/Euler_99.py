import re
import math

def primefactorize(num : int):
    return num

def compare_exponentials(num1 : list, num2 : list):
    # print()
    # print(num1)
    # print(num2)
    if (num1[0] == num2[0]):
        if num1[1] > num2[2]:
            return num1
        else:
            return num2

    elif (num1[0] > num2[0] and num1[1] > num2[1]):
        # print("num1[0] ({}) is bigger than num2[0] ({}) and num1[1] ({}) is bigger than num2[1] ({})".format(num1[0], num2[0], num1[1], num2[1]))
        return num1

    elif (num1[0] < num2[0] and num1[1] < num2[1]):
        # print("num1[0] ({}) is smaller than num2[0] ({}) and num1[1] ({}) is smaller than num2[1] ({})".format(num1[0], num2[0], num1[1], num2[1]))
        return num2

    else:
        pow_diff = math.log(num1[0]) / math.log(num2[0]) # -> num2[0] to the power of what equals num1[0]
        # print("pow_diff = {}".format(pow_diff))
        # print("pow1: {}, pow2: {} ".format(num1[1] * pow_diff, num2[1]))
        if (num1[1] * pow_diff > num2[1]):
            return num1
        else:
            return num2

def find_biggest_exponential(base_exp : list):
    if len(base_exp) == 1:
        return base_exp[0]
    elif len(base_exp) == 2:
        return compare_exponentials(base_exp[0], base_exp[1])
    else:
        return compare_exponentials(find_biggest_exponential(base_exp[:len(base_exp)//2]), find_biggest_exponential(base_exp[len(base_exp)//2:]))

if __name__ == "__main__":
    base_exp = open("Euler_99-base_exp.txt", "r").read()
    base_exp_list = [re.split(",", x) for x in re.split("\n", base_exp)]

    for x in range(len(base_exp_list)):
        for y in range(len(base_exp_list[x])):
            base_exp_list[x][y] = int(base_exp_list[x][y])
        base_exp_list[x].append(x + 1)

    # print(base_exp_list[0])
    biggest_exp = find_biggest_exponential(base_exp_list)
    print(biggest_exp)
    # line = base_exp_list.index(biggest_exp)

    print()