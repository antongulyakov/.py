#!/usr/bin/env python
# python3


import check


def is_year_leap(year):
    "Chek the leap year"
    if -45 <= year < -8:
        if year % 3 == 0:
            return True
    elif -8 <= year < 1582:
        if (year % 4 == 0) and (year is not 0):
            return True
    elif year >= 1582:
        if (year % 4 == 0) and (year % 100 is not 0):
            return True
        elif year % 400 == 0:
            return True
    else:
        return False

    return False

#year = check.input_num(1, 3)
year = check.input_digit(1, 3)
flag = is_year_leap(year)
print(flag)
