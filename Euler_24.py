# finding the millionth lexicographic permutations of numbers from 0 to 9 #
# lexicographic means listed in ascending numerical order or alphabetically

from itertools import permutations

perm = list(permutations([0,1,2,3,4,5,6,7,8,9]))

print(perm[999999])

