"""
:author: Anastasiia-Khab
:chapter: 4
: tasks: 86a, 107

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


def task107(m_int):
    """
    Given integer m_int >1. Returns max integer k, that 4**k<m_int
    :param m_int: type(m_int)==int
    :return: int k; 4**k<m_int;
    """
    k = 0
    while 4 ** k < m_int:
        k += 1
    return k - 1
