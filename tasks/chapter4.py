"""Chapter 4 tasks"""


def task_88a(num):
    """search for '3' in num**2"""
    sqr_n = num * num
    sqr_n = str(sqr_n)
    for num in sqr_n:
        if num == '3':
            return True

    return False
