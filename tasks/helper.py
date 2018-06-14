"""Helping functions for tasks"""


def sum_of_dividers(num):
    """returns the sum of number dividers"""
    dividers = list()
    for i in range(1, int(num / 2) + 2):
        if num % i == 0:
            dividers.append(i)

    _sum = 0
    for i in dividers:
        _sum += i

    return _sum


def is_perfect(num):
    """finds out whether num is a "perfect number" """
    res = bool(num == sum_of_dividers(num))
    return res
