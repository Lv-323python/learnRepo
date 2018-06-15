"""Chapter 15 tasks"""


def task_560():
    """finds all numbers-friends in [200, 300]"""
    result = dict()
    for i in range(200, 301):
        for j in range(200, 301):
            if i == _sum_of_dividers(j):
                result[i] = j

    return result


def _sum_of_dividers(num):
    """returns the sum of number dividers"""
    dividers = list()
    for i in range(1, int(num / 2) + 2):
        if num % i == 0:
            dividers.append(i)

    _sum = 0
    for i in dividers:
        _sum += i

    return _sum
