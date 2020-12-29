# finding the amount of triangular words in Euler_42-words

words = open('Euler_42-words.txt', 'r').read()

words = list(words[1:-1].split("\",\""))

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

triang = 0
counter = 1
triangset = set()

while triang < 14*26:
    
    triang += counter
    counter += 1
    triangset.add(triang)

counter = 0

for x in words:
    
    sumword = 0
    for y in range(len(x)):
        sumword += letdict[x[y]]
    
    if sumword in triangset:
        counter += 1

print(counter)