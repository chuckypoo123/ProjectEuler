# Finding the last 10 digits of the Marsenne prime 28433 * 2^7830457 + 1

def select_last_10_from(n):
    # Returns only the last 10 digits of the number given
    # Assuming that the size of the number is at least10 digits long
    return int(str(n)[-10:])

TRUNC_LEN = 10  # Number of digits we want to keep (from the least significant digit)
EXP_2 = 7830457

prime = 2
exponent = 1

while len(str(prime)) < TRUNC_LEN:
    prime *= prime
    exponent *= 2

basic_prime = prime
basic_exponent = exponent  # This should be 10

partial_product = 1
partial_product_exponent = 0
leftover_exponent = EXP_2
while partial_product_exponent + exponent < EXP_2:
    prime *= prime
    prime = select_last_10_from(prime) # We can truncate becauase only last 10 digits impact the themselves
    exponent *= 2
    if 2 * exponent > leftover_exponent:
        # Updating the partial product
        partial_product *= prime
        partial_product = select_last_10_from(partial_product)
        partial_product_exponent += exponent

        # Reseting prime and exponent
        leftover_power = EXP_2 - partial_product_exponent - basic_exponent
        if leftover_power < 0:
            pass
        else:
            
