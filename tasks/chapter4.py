"""
:authors: Anastasiia-Khab, Anna Bretsko, Partsey
:chapter: 4
: tasks: 86a, 107, 86b, 108, 88b

"""


def task_86_a(num):
    """
    Checks how many digits contains inputed natural number
    :param num: is >0 ; type(num)==int
    :return: >=0; int; how many digits contains num
    """
    number_of_digits = 1
    if (num - (num % 10)) > 0:
        number_of_digits += task_86_a((num - (num % 10)) / 10)
    return number_of_digits


def task_107(m_int):
    """
    Given integer m_int >1. Returns max integer k, that 4**k<m_int
    :param m_int: type(m_int)==int
    :return: int k; 4**k<m_int;
    """
    k = 0
    while 4 ** k < m_int:
        k += 1
    return k - 1


def task_86_b(num):
    """
    Takes natural number and returns the sum of digits of param.
    :param num: natural number
    :return: natural number
    """
    return sum(map(int, str(num)))


def task_108(num):
    """
    Takes a natural number anad returns the smallest number represented
    as 2^r which is greater than initial param.
    :param num: natural number
    :return: natural number
    """
    if num == 2:
        return 1
    elif num == 1:
        return 0
    return 2 ** (num - 1).bit_length()


def task_88_b(number):
    """
    Return number with reversed order of digits

    :param number: input number
    :return: reversed number
    """
    new_number = 0

    while number > 0:

        last_digit_number = number % 10

        new_number = new_number * 10 + last_digit_number

        number = number // 10

    return new_number
