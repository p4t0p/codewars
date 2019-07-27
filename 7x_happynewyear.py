def is_unique_digits(number): # number = 1234
    a = str(number) # a = '1234' 
    return a[0] != a[1] and a[0] != a[2] and a[0] != a[3] and a[1] != a[2] and a[1] != a[3] and a[2] != a[3]

def next_happy_year(year):
    year = year + 1
    while is_unique_digits(year) == False:
        year = year + 1
    return year 
