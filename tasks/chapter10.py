"""Chapter 10 tasks"""


def task_330(num):
    """finds all "perfect numbers" less than num"""
    result = list()
    for i in range(num):
        if _is_perfect(i):
            result.append(i)
    return result


def _sum_of_dividers(arg):
    """returns the sum of number dividers"""
    divs = list()
    for i in range(1, int(arg / 2) + 2):
        if arg % i == 0:
            divs.append(i)

    _suma = 0
    for i in divs:
        _suma += i

    return _suma


def _is_perfect(num):
    """finds out whether num is a "perfect number" """
    res = bool(num == _sum_of_dividers(num))
    return res
