"""Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True,
otherwise return False."""


def is_leap(year):
    leap = False
    if year % 100 == 0 and year % 400 == 0:
        leap = True
    if year % 4 == 0 and year % 100 != 0:
        leap = True
    return leap


if __name__ == '__main__':
    value = int(input())
    print(is_leap(value))
