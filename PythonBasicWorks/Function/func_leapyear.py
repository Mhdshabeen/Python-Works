

def is_leap_year(year):

    leap_year=False

    if (year%100==0 and year%400==0) or (year%100!=0 and year%4==0):

        leap_year=True

    return leap_year
    

print(is_leap_year(1600))