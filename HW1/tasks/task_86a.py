"""This module consists of group tasks."""


# task 86a
def task_86a(number: int) -> int:
    """
    Get digits length in the number
    :param number: int
    :return: int
    """
    if not isinstance(number, int):
        raise TypeError("Argument should be integer!")
    if number <= 0:
        raise ValueError("Argument is not natural number!")
    return len(str(number))