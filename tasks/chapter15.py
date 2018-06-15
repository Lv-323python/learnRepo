"""
:author: Anastasiia-Khab
:chapter: 15
: tasks: 554
"""


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
