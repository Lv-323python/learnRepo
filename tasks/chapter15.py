"""Chapter 15 tasks"""
from helper import sum_of_dividers


def task_560():
    """finds all numbers-friends in [200, 300]"""
    result = dict()
    for i in range(200, 301):
        for j in range(200, 301):
            if i == sum_of_dividers(j):
                result[i] = j

    return result
