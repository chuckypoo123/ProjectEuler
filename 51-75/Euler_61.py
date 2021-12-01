# Finding the sum of the 4-digit numbers in a 6-number cycle with triangular to octogonal numbers

# SOLVED
# Min time: 0.9 ms
import timeit

DEBUG = False

def printdebug(message):
    if DEBUG:
        print(message)

def triang_num(n):
    return n * (n + 1) // 2

def four_digit_triang():
    index = int((1000 * 2) ** 0.5) - 1
    triang_list = []
    triang = triang_num(index)
    while triang < 10000:
        triang_list.append(triang)

        index += 1
        triang = triang_num(index)

    printdebug(triang_list)

    return triang_list

def four_digit_square():
    index = 32 # Found by manually trying values
    square_list = []
    square = index * index
    while square < 10000:
        square_list.append(square)

        index += 1
        square = index * index

    printdebug(square_list)

    return square_list

def penta_num(n):
    return n * (3 * n - 1) // 2

def four_digit_penta():
    index = 26 # Found by manually trying values
    penta_list = []
    penta = penta_num(index)
    while penta < 10000:
        penta_list.append(penta)

        index += 1
        penta = penta_num(index)

    printdebug(penta_list)

    return penta_list

def hexa_num(n):
    return n * (2 * n - 1)

def four_digit_hexa():
    index = 23 # Found by manually trying values
    hexa_list = []
    hexa = hexa_num(index)
    while hexa < 10000:
        hexa_list.append(hexa)

        index += 1
        hexa = hexa_num(index)

    printdebug(hexa_list)

    return hexa_list

def hepta_num(n):
    return n * (5 * n - 3) // 2

def four_digit_hepta():
    index = 21 # Found by manually trying values
    hepta_list = []
    hepta = hepta_num(index)
    while hepta < 10000:
        hepta_list.append(hepta)

        index += 1
        hepta = hepta_num(index)

    printdebug(hepta_list)

    return hepta_list

def octa_num(n):
    return n * (3 * n - 2)

def four_digit_octa():
    index = 19 # Found by manually trying values
    octa_list = []
    octa = octa_num(index)
    while octa < 10000:
        octa_list.append(octa)

        index += 1
        octa = octa_num(index)

    printdebug(octa_list)

    return octa_list

# comparing the front of the current number (first 2 digits), with the back of the last number in cyclic_nums (last 2 digits)
def find_cycle_front(list_of_lists, listused, cyclic_nums):

    for i in range(5):
        if listused[i]:
            continue

        listused[i] = True

        for elem in list_of_lists[i]:
            
            if elem // 100 == cyclic_nums[-1] % 100:
                if len(cyclic_nums) == 5:
                    # print(cyclic_nums)
                    # print(elem)
                    # print(cyclic_nums[0] // 100)
                    # print(elem % 100)
                    # print()
                    if elem % 100 == cyclic_nums[0] // 100:
                        cyclic_nums.append(elem)
                        return cyclic_nums
                    else:
                        continue
                
                # print(cyclic_nums)
                cyclic_nums.append(elem)
                result = find_cycle_front(list_of_lists, listused, cyclic_nums)
                if len(result) == 6:
                    return result
                cyclic_nums.pop(-1)

        listused[i] = False

    return cyclic_nums
            
def main():
    start = timeit.default_timer()
    geo_list = [four_digit_triang(), four_digit_square(), four_digit_penta(), four_digit_hexa(), four_digit_hepta()]
    geo_list.reverse()
    octalist = four_digit_octa()
    listused = [False for x in range(5)]

    for num in octalist:
        cyclic_num = [num]
        after_check = find_cycle_front(geo_list, listused, cyclic_num)

        if len(after_check) == 6:
            print(after_check)
            print(sum(after_check))
            break
    
    print("Time taken: " + str(timeit.default_timer() - start) + "s")

# print(four_digit_triang())
# print()
# print(four_digit_square())
# print()
# print(four_digit_penta())
# print()
# print(four_digit_hexa())
# print()
# print(four_digit_hepta())
# print()
# print(four_digit_octa())

# list1 = [1, 2, 3, 4, 5]
# list2 = list1
# list2.remove(list2[2])
# print(list2)
# print(list1)

main()