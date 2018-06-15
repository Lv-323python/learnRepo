"""
:authors: Anastasiia-Khab, Anna Bretsko
:chapter: 7
: tasks: 224, 225

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
    for natural in range(1, int(num + 1)):
        if num % natural == 0:
            dividers.append(natural)
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
