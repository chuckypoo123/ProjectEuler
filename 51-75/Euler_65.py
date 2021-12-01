# Finding the sum of digits of the numerator of the 100th convergence of e
# We are given that the infinite fraction of e can be represented as follows
# e = [2; 1, 2, 1, 1, 4, 1, 1, 6, 1, ..., 1, 2k, 1, ...]
# The infinite fraction is as follows e[0] + 1/ (e[1] + 1/ (e[2] + 1/...))

def conv_of_e(nth_conv = 100):
    e = [(((x - 2) // 3) + 1) * 2 if (x - 2) % 3 == 0 else 1 for x in range(nth_conv)]
    e[0] = 2
    e.reverse()
    print(e)

    num = 1
    denom = e[0]
    for i in range(1, nth_conv):
        past_num = num
        num = denom
        denom = e[i]*denom + past_num

    temp = num
    num = denom
    denom = temp

    print("Numerator:   " + str(num))
    print("Denominator: " + str(denom))
    print("Floating point: " + str(num/denom))
    return (num, denom)

def sum_digits(num):
    total = 0
    while num != 0:
        total += num % 10
        num //= 10

    return total

if __name__ == "__main__":
    print(sum_digits(conv_of_e(100)[0]))