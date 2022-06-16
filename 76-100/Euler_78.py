# def coin_arrangement(n, max_group_size = 0):
#     if max_group_size == 0: max_group_size = n
    
#     if n == 0: return 1
#     if n == 1: return 1
#     if max_group_size == 1: return 1
    
#     total = 0
#     for biggest_group in range(1, n+1):
#         # for group in range(1, biggest_group + 1):
#             total += coin_arrangement(n - biggest_group, biggest_group)

#     print(f"N: {n}, max_group_size: {max_group_size}, total: {total}")
#     return total

def pile_permutations(n, n_piles, max_per_pile):
    if n_piles == 0: return 0
    if n == 0: return 1
    if n == 1: return 1

    total = 0
    for new_max_per_pile in range(1, max_per_pile + 1):
        total += pile_permutations(n - new_max_per_pile, n_piles - 1, new_max_per_pile)

    return total

def coin_arrangement(n):
    total = 0
    for n_piles in range(1, n):
        total += pile_permutations(n, n_piles, n)

    return total

if __name__ == "__main__":
    print(coin_arrangement(5))