# finding the number of Sundays that were the first of a month in the
# twentieth century (1 Jan 1901 to 31 Dec 2000) #

counter = 0

day = 2 # day 0 is a Sunday, Jan 1 1901 was a Tuesday, so day 2 in the week

days_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

days_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for x in range(25):
    
    for y in range(3):
        for z in range(12):
            day += days_year[z]
            if day % 7 == 0:
                counter+= 1
    
    for w in range(12):
            day += days_year[w]
            if day % 7 == 0:
                counter+= 1
        
print(counter)