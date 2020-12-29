# finding the sum of all even fibonacci numbers under 4,000,000 #

var1=1
var2=2
var3=0
total=2

while var3 <= 4000000:
    var3 = var1 + var2

    var1 = var2
    var2 = var3
    var3 = var1 + var2

    var1 = var2
    var2 = var3
    var3 = var1 + var2

    var1 = var2
    var2 = var3

    if var3 < 4000000 :
        total += var3

print(total)