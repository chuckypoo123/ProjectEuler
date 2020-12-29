# finding the amount of hands player 1 will win in the following file #

hands = open("Euler_54-poker.txt", "r").read()

hands = list(hands.split("\n"))

hands = hands[:-1]

def getkey(val, dict1):
    for key, value in dict1.items():
        if val == value:
            return key

def rankhand(a, b):
    
    if len(b) == 1: # if there is only 1 suit:
        for x in range(len(a) - 1):
            if a[x] - a[x + 1] != 1: # if numbers are not consecutive:
                rank = a[0] * 10**9 # flush
                break
        else: # If all numbers are consecutive
            rank = a[0] * 10**12 #straight/royal flush

    else:
        for x in range(len(a) - 1):
            if a[x] - a[x + 1] != 1: # if numbers are not consecutive
                count = {i:a.count(i) for i in a}
                if 4 in count.values(): # four of a kind
                    rank = getkey(4, count) * 10**11 + getkey(1, count) 
                    
                elif 3 in count.values() and 2 in count.values():
                    # full house
                    rank = getkey(3, count) * 10**10 + getkey(2, count)
                    
                elif 3 in count.values() and 2 not in count.values():
                    # 3 of a kind
                    nottrip = list(set(a))
                    nottrip.remove(getkey(3, count))
                    nottrip.sort()
                    rank = getkey(3, count) * 10**7
                    for x in range(len(nottrip)):
                        rank += nottrip[x] * 10**x
                    
                elif 2 in count.values() and 3 not in count.values():
                    count2 = [count[i] for i in count]
                    countpair = {j:count2.count(j) for j in count2}
                    
                    if countpair[2] == 2: # 2 pairs
                        a.remove(getkey(1, count))
                        a = list(set(a))
                        a.sort()
                        rank = a[1] * 10**6 + a[0] * 10 + getkey(1, count)
                        
                    elif countpair[2] == 1: # 1 pair
                        notpair = list(set(a))
                        notpair.remove(getkey(2, count))
                        notpair.sort()
                        rank = getkey(2, count) * 10**5
                        for x in range(len(notpair)):
                            rank += notpair[x] * 10**x
                        
                else: #highest card
                    rank = 0
                    for x in range(5):
                        rank += a[x] * 10**(4 - x)
                break
        else:
            rank = a[0] * 10**8 # straight
            
    return rank

figdict = {
    "T" : 10,
    "J" : 11,
    "Q" : 12,
    "K" : 13,
    "A" : 14
    }

p1wins = 0
p2wins = 0

for x in range(len(hands)):
    hands[x] = list(hands[x].split(" "))
    
    p1 = hands[x][:5]
    p2 = hands[x][5:]
    
    p1suit = set()
    for l in p1:
        p1suit.add(l[-1])
        
    p1num = [figdict[m[0]] if m[0] in figdict else int(m[0]) for m in p1]
    p1num.sort(reverse = True)
    
    
    p2suit = set()
    for n in p2:
        p2suit.add(n[-1])
        
    p2num = [figdict[o[0]] if o[0] in figdict else int(o[0]) for o in p2]
    p2num.sort(reverse = True)
    
    p1rank = rankhand(p1num, p1suit)
    p2rank = rankhand(p2num, p2suit)
    
    if p1rank > p2rank:
        p1wins += 1

    else:  
        p2wins += 1
    
print(p1wins, p2wins)