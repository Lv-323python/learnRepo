"""Chapter 10 tasks"""
from helper import is_perfect


def task_330(num):
    """finds all "perfect numbers" less than num"""
    result = list()
    for i in range(num):
        if is_perfect(i):
            result.append(i)
    return result
