'''
Consider quadratic Diophantine equations of the form:

x^2 - Dy^2 = 1

For example, when D=13, the minimal solution in x is 649^2 - 13×180^2 = 1.

It can be assumed that there are no solutions in positive integers when D is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

3^2 - 2*2^2 = 1
2^2 - 3*1^2 = 1
9^2 - 5*4^2 = 1
5^2 - 6*2^2 = 1
8^2 - 7*3^2 = 1

Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.

Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.
'''

'''
To find a D's minimal solution:
Iterate through y's (increase y's until you find a solution)
Start x from the biggest square below D
Compare x^2 to D*y^2 + 1
-> If x^2 == D*y^2 + 1
-> If x^2 is smaller, increase the value of x 
-> If x^2 is bigger increase y and restart x (maybe not restart x)
'''
import timeit

def min_x_y(D: int, biggest_smaller_square: int = 1):
    y = 1
    x = biggest_smaller_square
    start = timeit.default_timer()
    try:
        while True:
            if x*x == D * y * y + 1:
                return [x, y, timeit.default_timer() - start]
            elif x*x < D * y * y + 1:
                x += 1
            else:
                y += 1
    except KeyboardInterrupt:
        print("Interrupt")
        print(D, biggest_smaller_square)
        print(x, y, f"Time taken: {timeit.default_timer() - start}")

def min_x_y_sum(D: int, biggest_smaller_square: int = 1):
    y = 1
    Dy21 = D * y * y + 1
    x = biggest_smaller_square + 1
    x2 = x * x
    start = timeit.default_timer()
    try:
        while True:
            if x2 == Dy21:
                return [x, y, timeit.default_timer() - start]
            elif x2 < Dy21:
                x2 += 2 * x + 1
                x += 1
            else:
                Dy21 += D * (2 * y + 1)
                y += 1
    except KeyboardInterrupt:
        print("Interrupt")
        print(D, biggest_smaller_square)
        print(x, y)
        print(x, y, f"Time taken: {timeit.default_timer() - start}")

def main():
    previous_root = 1
    D_with_max_x = 1
    max_x = 1

    for i in range(2, 1000):
        if i == previous_root * (previous_root + 2) + 1:
            previous_root += 1
            continue

        if i == 61 or i == 97 or i == 106:
            continue

        D_x_y = min_x_y_sum(i)
        print(i, D_x_y)
        if D_x_y[0] > max_x:
            max_x = D_x_y[0]
            D_with_max_x = i

    return D_with_max_x

if __name__ == "__main__":
    # print("D with max x", main())

    print(min_x_y(61))
    # print(min_x_y_sum(7))

# Numbers posing issues: 61, 97, 106, 109