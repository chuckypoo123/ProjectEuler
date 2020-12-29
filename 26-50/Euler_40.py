str1 = ""
var = 0
while len(str1) < 1000001:
    str1 += str(var)
    var += 1
    
print(str1[1], str1[10], str1[100], str1[1000], str1[10000], str1[100000],\
      str1[1000000])
    