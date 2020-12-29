# finding the sum of all the multiples of 3 and 5 under 1000 #

variable_1 = 3
total_1 = 0
while variable_1 < 1000:
    total_1 += variable_1
    variable_1 = variable_1 + 3

variable_2 = 5
total_2 = 0
while variable_2 < 1000:
    total_2 += variable_2
    variable_2 = variable_2 + 5

variable_3 = 15
total_3 = 0
while variable_3 < 1000:
    total_3 += variable_3
    variable_3 = variable_3 + 15

total = total_1 + total_2 - total_3

print(total_1, total_2, total_3, total, sep=", ")