"""Chapter 4 tasks"""


def task_88a(arg):
    """search for '3' in arg**2"""
    sqr_n = arg * arg
    sqr_n = str(sqr_n)
    for num in sqr_n:
        if num == '3':
            return True

    return False
