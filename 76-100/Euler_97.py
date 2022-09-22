# Finding the last 10 digits of the Marsenne prime 28433 * 2^7830457 + 1

def select_last_10_from(n):
    # Returns only the last 10 digits of the number given
    # Assuming that the size of the number is at least10 digits long
    return int(str(n)[-10:])

TRUNC_LEN = 10  # Number of digits we want to keep (from the least significant digit)
MULT_EXP_2 = 28433
EXP_2 = 7830457
# EXP_2 = 347

prime = 2
exponent = 1

while len(str(prime)) < TRUNC_LEN:
    prime *= prime
    exponent *= 2

basic_prime = prime
basic_exponent = exponent  # This should be 32

partial_product = 1
partial_product_exponent = 0
leftover_exponent = EXP_2
while True:
    prime *= prime
    prime = select_last_10_from(prime) # We can truncate becauase only last 10 digits impact themselves
    exponent *= 2
    if partial_product_exponent + 2 * exponent >= EXP_2: # If next iteration of loop would exceed target
        # Updating the partial product
        partial_product *= prime
        partial_product = select_last_10_from(partial_product)
        partial_product_exponent += exponent

        # Reseting prime and exponent
        if partial_product_exponent > EXP_2 - basic_exponent*2: # We cannot start from the 10-digit found above
            if partial_product_exponent != EXP_2:
                partial_product <<= EXP_2 - partial_product_exponent # Left-shift by missing powers of 2
            prime = select_last_10_from(partial_product)
            exponent = EXP_2
            break
        else:
            prime = basic_prime
            exponent = basic_exponent

            
# print(prime)
# print(exponent)

prime *= MULT_EXP_2
prime += 1
prime = select_last_10_from(prime)

print(prime)
