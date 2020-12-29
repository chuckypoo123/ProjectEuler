# finding the first triangular number with 500 divisors #

triang = 0
add = 1
div = []

while len(div) <= 5:
    
    triang += add
    add += 1
    div = [1, triang]
    var = 2
    while var < triang:
        if triang%var == 0:
            div.append(var)
        var += 1
    
print(triang)

# this would work, but takes WAY too much time. 