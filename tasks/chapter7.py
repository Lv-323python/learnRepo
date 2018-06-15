"""Chapter 7 tasks"""
from math import sqrt


def task_178c(*num):
    """counts the square roots of even numbers in list"""
    count = 0
    for num in num:
        if sqrt(num) % 2 == 0:
            count += 1
    return count


def task_227(var1, var2):
    """finds all the dividers of the parameters"""
    result = list()
    if var1 == 0 or var2 == 0:
        result.append("No zeros in input!")
        return result

    for i in range(1, int(min(var1, var2) / 2) + 2):
        if var1 % i == 0 and var2 % i == 0:
            result.append(i)

    return result
