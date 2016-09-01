def day_of_month(x):
	return (28 + (x + x//8) % 2 + 2 % x + 2 * (1//x))


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


def real_date():
    date = input("input date dd.mm.yyyy:").split(".")
    date = [int(x) for x in date]
    if date[1]>12:
        return False
    if date[1] == 2 and is_year_leap(date[2]):
        day = 29
    else:
        day = day_of_month(date[1])
    if date[0] <= day:
        return True
    else:
        return False
