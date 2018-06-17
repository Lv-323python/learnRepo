"""
:authors: Anastasiia-Khab, Anna Bretsko, mixa1901
:chapter: 7
: tasks: 182, 224, 225, 241

"""
from math import sqrt


def task_224(num):
    """
    Дано натуральное число n. Получить все его натуральные делители.
    :param num: natural
    :return: tuple of all natural dividers of num
    """
    dividers = []
    if num == 0:
        return [0]
    for natural in range(1, int(num + 1)):
        if num % natural == 0:
            dividers.append(natural)
    return dividers



def task_225(num):
    """
    Takes natural number returns every q if parameter is divided
    by q power of two but not divided by q power of three.
    :param num: natural number
    :return: list of natural numbers
    """
    return [q_num for q_num in range(1, (num + 1))
            if not num % (q_num ** 2) and num % (q_num ** 3)]


def task_182(num):
    """
    get amount and sum of sequence of numbers
    from 1 to num that are not divisible by 7 and divisible by 5
    :param num: int
    :return: string
    """
    # get list of items which are not divisible by 7 and divisible by 5
    a_list = [i for i in range(1, num+1) if i % 5 == 0 and i % 7 != 0]

    # get amount of the items and sum
    amount = len(a_list)
    sum_of_a = sum(a_list)

    # return resulting string
    return "Amount: " + str(amount) + " Sum: " + str(sum_of_a)


def task_241(num, x_num):
    """
    get mathematical result of given mathematical task
    :param num: int
    :param x_num: int
    :return: float
    """
    result = 0

    # iterate through given amount of integers
    for i_num in range(1, num+1):
        result += (-1 ** sqrt(i_num)) / i_num * (x_num ** i_num)

    return result
