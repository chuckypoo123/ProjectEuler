# finding the position of the first fibonacci number with 1000 digits #

fib1 = 1
fib2 = 1
counter = 2     # counter starts at 2 because the first newfib will be the
fiblen = False  # third fibonacci number

while fiblen is False:
    
    newfib = fib1 + fib2
    counter += 1
    fib1 = fib2
    fib2 = newfib
    
    if len(str(newfib)) == 1000:
        fiblen = True
    
print(counter)