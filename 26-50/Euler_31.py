# finding the number of ways to arrange 1, 2, 5, 10, 20, 50, 100, 200 to make
# 200 #

coins = [1, 2, 5, 10, 20, 50, 100, 200]
coins.reverse()

def sumways(k, c) :
    result = 0
    if k == 0:
        result = 1
    elif k < 0 :
        result = 0
    else:
        for x in coins[c:]:
            result += sumways(k - x, coins.index(x))
            
    return result

print(sumways(200, 0))