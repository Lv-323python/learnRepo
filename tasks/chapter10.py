"""
:authors: Anastasiia-Khab, Anna Bretsko
:chapter: 7
: tasks: 323, 325
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
        if _gcd(natural, num) == 1:
            naturals.append(natural)
    return naturals


def _gcd(num1, num2):
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


def task_325(num):
    """
    Takes input of natural number and returns all its primes dividers.
    :param num: natural number
    :return: list of prime numbers
    """
    naturals = []
    if num == 0:
        naturals.append(0)
    for natural in range(1, num + 1):
        if _gcd(natural, num) == natural:
            check_if_divide = True
            for natural1 in range(2, natural):
                if _gcd(natural1, natural) == natural1:
                    check_if_divide = False
            if check_if_divide:
                naturals.append(natural)
    return naturals
