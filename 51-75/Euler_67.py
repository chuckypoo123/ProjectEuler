# finding the path with the biggest sum in this 100-row pyramid #

pyr = open("Euler_67-triangle.txt", "r").read()

pyr = pyr[:-1]

pyr = list(pyr.split("\n"))

for x in range(len(pyr)):
    pyr[x] = list(pyr[x].split(" "))
    
    for y in range(len(pyr[x])):
        pyr[x][y] = int(pyr[x][y])
        
pyr.reverse()
        
for x in range(1, len(pyr)):
    for y in range(len(pyr[x])):
        a = pyr[x][y] + pyr[x-1][y]
        b = pyr[x][y] + pyr[x-1][y+1]
        if a >= b:
            pyr[x][y] = a
        else:
            pyr[x][y] = b

print(pyr[-1][-1])