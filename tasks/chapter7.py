"""
:authors: Anastasiia-Khab, Anna Bretsko, Partsey, Ihor Soroka
:chapter: 7
: tasks: 224, 225, 178g, 243, 178_b, 226

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



def task_178_g(sequence_len, *args):
    """
    Return the number of elements of sequence that satisfy condition a[k] < ( a[k-1] + a[k+1] ) / 2

    :param sequence_len: length of sequence
    :param args: sequence of numbers
    :return:number of elements
    """
    counter = 0

    for k in range(1, sequence_len-1):
        if args[k] < (args[k-1] + args[k+1]) / 2:
            counter = counter + 1

    return counter


def task_243(number):
    """
    Return a pair of numbers (x, y) if exists so that number = x**2 + y**2

    :param number: input number
    :return: pair of numbers or False
    """
    if not (number ** 0.5).is_integer():
        return False

    found = False
    number_x = 0
    number_y = 0

    x_val = 1
    while x_val < number and not found:
        y_val = x_val + 1
        while y_val < number and not found:
            if number == x_val**2 + y_val**2:
                number_x = x_val
                number_y = y_val
                found = True

            y_val = y_val + 1
        x_val = x_val + 1

    if found:
        return number_x, number_y
    return False


def task_178_b(*args):
    '''
    There are given natural numbers n, a.1, ..., a.n. Determine the number of members of
        multiple 3 and non-multiple 5 a.k sequences a.1, ..., a.n.

    :param args: int - natural numbers.
    :return: int - natural number.
    '''

    amount = 0
    for arg in args:
        if arg % 3 == 0 and arg % 5 != 0:
            amount += 1
    return amount


def task_226(nnumber, mnumber):
    '''
    There are given natural numbers m, n. Get all of them
        natural total multiples, less m * n.

    :param nnumber: int - natural number.
    :param mnumber: int - natural number.
    :return: list: int natural numbers.
    '''

    deduction = max(nnumber, mnumber)
    start = mnumber * nnumber - deduction
    amount = []
    while start >= nnumber and start >= mnumber:
        if start % nnumber == 0 and start % mnumber == 0:
            amount.append(start)
        start -= deduction
    return amount
