"""
:authors: Anastasiia-Khab, Anna Bretsko, Bondar Artem
:chapter: 7
: tasks: 224, 225, 243b

"""


def task_224(num):
    """
    Дано натуральное число n. Получить все его натуральные делители.
    :param num: natural
    :return: tuple of all natural dividers of num
    """
    dividers = []
    if num == 0:
        return [0]
    dividers.append(1)
    for natural in range(2, int(num + 1)):
        if num % natural == 0:
            dividers.append(natural)
            dividers += task_224_find_other_dividers(int(num / natural))
            break
    return dividers


def task_224_find_other_dividers(num):
    """
    Дано натуральное число n. Получить все его натуральные делители.
    :param num: natural
    :return: tuple of all natural dividers of num
    """
    dividers = []
    for natural in range(2, int(num + 1)):
        if num % natural == 0:
            dividers.append(natural)
            dividers += task_224_find_other_dividers(int(num / natural))
            break
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


def task_178_d(startn=0, lastn=0):
    """
    Function which finds all numbers in range a^k<ak<k!
    """
    import math
    count = 0
    for k in range(startn, lastn + 1):
        ind = 1
        if k > 2 ** ind:
            if math.factorial(k) > k:
                count = count + 1
        ind += 1
    return count

def task_243_b(num=0):
    """
    Function which finds sum of sqrt of the number
    """
    answrs = []
    for x_num in range(0, num):
        for y_num in range(0, num):
            if (x_num * x_num + y_num * y_num) == num:
                values_xy = [x_num, y_num]
                answrs.append(values_xy)
    return answrs
