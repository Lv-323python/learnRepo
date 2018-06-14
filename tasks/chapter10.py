"""
:authors: Anastasiia-Khab, Anna Bretsko, Partsey
:chapter: 7
: tasks: 323, 325, 331
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


def task_331(number):
    """
    Return a pair of numbers (x, y) if exists so that number = x**2 + y**2

    :param number: input number
    :return: pair of numbers or False
    """
    if not (number ** 0.5).is_integer():
        return False

    found = False
    number_a = 0
    number_b = 0
    number_c = 0

    a_val = 1
    while a_val < number and not found:
        b_val = a_val + 1
        while b_val < number and not found:
            c_val = b_val + 1
            while c_val < number and not found:
                if number == a_val ** 2 + b_val ** 2 + c_val ** 2:
                    number_a = a_val
                    number_b = b_val
                    number_c = c_val
                    found = True
                c_val = c_val + 1
            b_val = b_val + 1
        a_val = a_val + 1

    if found:
        return number_a, number_b, number_c

    return False
