# finding the amount of letters in all numbers until 1000 (inclusive) when
# spelled out (ignoring spaces and including "and") #

a = """one two three four five six seven eight nine""" # 8 spaces
b = """ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen
nineteen""" # 9 spaces
c = """twenty thirty forty fifty sixty seventy eighty ninety""" # 7 spaces
d = """hundred"""
e = """thousand"""
f = """and"""

sum1 = len("one") + len(e) # one thousand
sum2 = (len(a) - 8)*100 + len(d)*900 + len(f)*891 # "x hundred and"
sum3 = 10*((len(c) - 7)*10 + len(b) - 9 + (len(a) - 8)*9) # inside a hundred
total = sum1 + sum2 + sum3

print(total)