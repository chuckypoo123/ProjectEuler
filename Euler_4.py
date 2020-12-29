# finding the biggest palindrome that is the product of 2 3-digit numbers #
list1 = []
var1 = 999
var2 = 999

while var1 >= 900:

    while var2 >= 900:

        result = var1*var2
        str_result = str(result)
        if str_result[0] == str_result[5] and str_result[1] == str_result[4]\
            and str_result[2] == str_result[3]:
            list1.append(result)
        var2 -= 1

    var1 -= 1
    var2 = var1

list1.sort(reverse=True)
print(list1[0])