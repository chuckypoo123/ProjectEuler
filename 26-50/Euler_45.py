# finding the number after 40755 that is triangular, pentagonal and
# hexagonal #

tricount = 286 # 1 index higher than 40755
pencount = 166
hexcount = 144

def newtri(n):
    global tri, tricount
    tri = int((n * (n + 1)) / 2)
    tricount += 1
    
def newpen(n):
    global pen, pencount
    pen = int((n * (3 * n - 1)) / 2)
    pencount += 1

def newhex(n):
    global hexa, hexcount
    hexa = int(n * (2 * n - 1))
    hexcount += 1

newtri(tricount)
newpen(pencount)
newhex(hexcount)

notfound = True

while notfound is True:
    num = [tri, pen, hexa]
    num.sort()
    
    if tri == pen == hexa:
        print(tri)
        notfound = False
        
    elif tri == num[0]:
        newtri(tricount)
        
    elif pen == num[0]:
        newpen(pencount)
        
    elif hexa == num[0]:
        newhex(hexcount)