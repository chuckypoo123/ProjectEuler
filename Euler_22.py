# finding the sum of the name scores in names.txt #

names = open('Euler_22-names.txt', 'r').read()

names = sorted(list(names[1:-1].split("\",\"")))

letdict = {
    "A":1,
    "B":2,
    "C":3,
    "D":4,
    "E":5,
    "F":6,
    "G":7,
    "H":8,
    "I":9,
    "J":10,
    "K":11,
    "L":12,
    "M":13,
    "N":14,
    "O":15,
    "P":16,
    "Q":17,
    "R":18,
    "S":19,
    "T":20,
    "U":21,
    "V":22,
    "W":23,
    "X":24,
    "Y":25,
    "Z":26}

sum1 = 0

for x in range(len(names)):
    
    namemult = 0
    
    for y in range(len(names[x])):
        
        namemult += letdict[names[x][y]]
        
    
    sum1 += (x + 1)*namemult
    
print(sum1)
    