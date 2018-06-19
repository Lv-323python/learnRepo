"""
:authors: Anastasiia-Khab, Anna Bretsko, Partsey
:chapter: 15
: tasks: 554, 555, 562
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



def task_562(n_val):
    """
    Return all numbers less or equal to n_val if last digits of number**2 == number

    :param n_val: max possible number
    :return: list of numbers that satisfy condition
    """
    matched_numbers = list()

    for number in range(1, n_val + 1):
        number_copy = number

        squared = number * number

        match = True
        while number > 0:
            last_digit_number = number % 10
            last_digit_squared = squared % 10

            if last_digit_number != last_digit_squared:
                match = False
                break

            number = number // 10
            squared = squared // 10

        if match:
            matched_numbers.append(number_copy)

    return matched_numbers
