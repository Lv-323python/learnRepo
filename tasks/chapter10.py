"""
:author: Anastasiia-Khab
:chapter: 7
: tasks: 323
"""


def task_323(num):
    """
    Дано натуральное число n. Получить все натуральные числа, меньшие n и взаимно простые с ним.
    :param num: natural
    :return: list of natural numbers n, n<num, gcd(n,num)=0
    """
    naturals = []
    if num == 0:
        naturals.append(0)
    for natural in range(1, num):
        if gcd(natural, num) == 1:
            naturals.append(natural)
    return naturals


def gcd(num1, num2):
    """
    Calculate the Greatest Common Divisor of num1 and num2.

    Unless num2==0, the result will have the same sign as num2 (so that when
    num2 is divided by it, the result comes out positive).

    :param num1: natural number
    :param num2: natural number
    :return: natural number
    """
    while num2:
        num1, num2 = num2, num1 % num2
    return num1
