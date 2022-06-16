from math import gcd

def sqrt_as_fraction(n: int):
    frac = []
    frac_data = []
    closest_smaller_sqrt = int(n**0.5)
    # frac.append(closest_smaller_sqrt)

    num_mult = 1
    num_addend = closest_smaller_sqrt
    denom = n - closest_smaller_sqrt*closest_smaller_sqrt

    while True:
        # Compute next item in continued fraction
        iterations = 0
        while -num_addend <= closest_smaller_sqrt:
            num_addend -= denom
            iterations += 1

        num_addend += denom
        iterations -= 1

        current_frac_data = [iterations, num_mult, num_addend, denom]
        if current_frac_data in frac_data:
            break
        frac.append(iterations)
        frac_data.append(current_frac_data)

        # Update fraction
        num_addend = -num_addend
        num_mult = denom
        denom = n - num_addend*num_addend
        # Reduce fraction
        gcd_nd = gcd(num_mult, denom)
        num_mult //= gcd_nd
        denom //= gcd_nd
    
    # print(f"{n}: {frac}, {len(frac)}")
    return frac

def count_odd_period(n):
    odds = 0

    smaller_sqrt = 1
    next_square = 4
    
    for i in range(2, n+1):
        if i == next_square:
            smaller_sqrt += 1
            next_square += 2*smaller_sqrt + 1
            # print(next_square)
            continue

        if len(sqrt_as_fraction(i)) % 2 == 1:
            # print(i)
            odds += 1

    return odds


if __name__ == "__main__":
    # print(sqrt_as_fraction(4))
    print(count_odd_period(10000))
    
    # sqrt_as_fraction(9997)

# Example:
# Use 23
# sqrt(23) = 4 + sqrt(23) - 4
#          = 4 + 1/ 1/(sqrt(23) - 4)
#          = 4 + 1/ (sqrt(23) + 4)/7
#          = 4 + 1/ (1 + (sqrt(23) - 3)/7)
#
# Procedure:
#   1. Add and subtract highest possible number (find biggest square below number under sqrt)
#   2. Do 1/ 1/(sqrt(x) - floor(sqrt(x)))
#   3. Rationalize denominator 1/ (sqrt(x) + floor(sqrt(x)))/(x - floor(sqrt(x))^2)