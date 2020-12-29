set1 = set()
for a in range(2, 101):
    for b in range(2, 101):
        set1.add(a**b)
        
print(len(set1))