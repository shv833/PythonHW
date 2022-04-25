# task 86b
def task_86b(number: int) -> int:
    """
    Get digits sum in the number
    :param number: int
    :return: int
    """
    if not isinstance(number, int):
        raise TypeError("Argument should be integer!")
    if number <= 0:
        raise ValueError("Argument is not natural number!")
    return sum([int(num) for num in str(number)])
