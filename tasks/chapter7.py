"""
:author: Anastasiia-Khab
:chapter: 7
: tasks: 224

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
