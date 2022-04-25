"""This module contains realisation of task 182."""
def is_natural_number(number: int) -> bool:
    """
    Returns True if the number is natural.
    """
    return isinstance(number, int) and number > 0

def has_int_in_list(array: list[int]) -> bool:
    """
    Returns True if the list has integer elements.
    """
    tmp: bool
    for i in array:
        if not isinstance(i, int):
            return False
        tmp = True

    return tmp

def task_182(number: int, array: list[int]) -> tuple:
    """
    Returns amount and sum of elements
        which are divisible by 5 and not divisible by 7.
    """
    assert is_natural_number(number), "The number should be natural"
    assert has_int_in_list(array), "The list should have integer elements"

    amount = 0
    sum_res = 0

    for i in range(0, number):
        if array[i] % 5 == 0 and array[i] % 7 != 0:
            amount += 1
            sum_res += array[i]

    return amount, sum_res
