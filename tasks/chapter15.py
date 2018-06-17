"""
:authors: Anastasiia-Khab, Anna Bretsko, mixa1901
:chapter: 15
: tasks: 554, 555, 568
"""
from itertools import product
from ast import literal_eval


def task_554(num):
    """
    Дано натуральное число n. Получить все пифагоровы тройки натуральных чисел,
    каждое из которых не превосходит n, т. е. все такие тройки натуральных чисел
    a, b, c, что a 2 + b 2 = c 2 (a ≤ b ≤ c ≤ n).
    :param num: natural number
    :return: list of tupels 3 natural number each
    """
    pifagors_triangles = []
    for natural_1 in range(1, num+1):
        for natural_2 in range(1, num+1):
            natural_3 = (natural_1 ** 2 + natural_2 ** 2) ** 0.5
            if natural_3 <= num and \
                    natural_3 % 1 == 0:
                pifagors_triangles.append((natural_1, natural_2, int(natural_3)))

    return pifagors_triangles


def task_555(num):
    """
    Takes natural number and returns the number of lines of Pascal's Triangle
    :param num: natural number
    :return: list of lists
    """
    triangle = []
    res = []
    for _ in range(num):
        res = [1 if i == 0 or i == len(res) else res[i - 1] + res[i] for i in range(len(res) + 1)]
        triangle.append(res)
    return triangle


def task_568(m_num):
    """
    check if given number can be gotten by inserting +, -
    into 1,2,3,4,5,6,7,8,9 sequence between different numbers
    :param m_num: int
    :return: str
    """

    sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # add %s between numbers in order to insert particular signs
    expr = '%s'.join([str(number) for number in sequence])

    signs = ["+", "-", ""]

    # iterate through every possible combination of sighns
    for item in product(signs, repeat=len(sequence) - 1):

        # get expression by inserting signs
        full_expr = expr % item

        # check if expression matches given number
        if literal_eval(full_expr) == m_num:
            return '%s=%s' % (full_expr, m_num)

    return "It's not possible to get %s from 1, 2, 3, 4, 5, 6, 7, 8, 9 sequence" % m_num
