"""Chapter 10 tasks"""
from helper import is_perfect


def task_330(number):
    """finds all "perfect numbers" less than number"""
    result = list()
    for i in range(number):
        if is_perfect(i):
            result.append(i)
    return result
