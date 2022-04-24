"""This module let us check algotasks:)"""
import random


def is_natural_number(number: int) -> bool:
    """
    Returns True if the number is natural
    """
    return isinstance(number, int) and number > 0

def has_int_in_list(array: list[int]) -> bool:
    """
    Returns True if the list has integer elements
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
        which are divisible by 5 and not divisible by 7
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

def task_323(number: int) -> list:
    """
    Returns all natural numbers less than n and coprime with it
    """
    assert is_natural_number(number), "The number should be natural"

    tmp = number - 1
    array = []
    while tmp != 0:
        for i in range(tmp, 0, -1):
            tmp1 = tmp
            tmp2 = i
            while tmp2 != 0 and tmp1 != 0:
                if tmp2 > tmp1:
                    tmp2 = tmp2 % tmp1
                else:
                    tmp1 = tmp1 % tmp2

            if tmp2 + tmp1 == 1:
                array.append(str(tmp) + ' & ' + str(i))
        tmp -= 1
    return array

def task_560() -> list:
    """
    Returns all pairs of friendly numbers between 200 and 300
    """
    tmp = 0
    array = []
    for k in range(200, 301):
        if k != tmp:
            sum1 = 0
            for i in range(1, k):
                if k % i == 0:
                    sum1 += i

            sum2 = 0
            for j in range(1, sum1):
                if sum1 % j == 0:
                    sum2 += j

            if sum2 == k != sum1:
                array.append(str(k) + ' ' + str(sum1))
                tmp = sum1
    return array


if __name__ == "__main__":
    NUMBER = 5
    random_list = []

    assert is_natural_number(NUMBER), "Number should be natural"

    while len(random_list) != NUMBER:
        random_list.append(random.randint(1, 100))

    assert has_int_in_list(
        random_list), "The list should have integer elements"

    print("Task182: ")
    print("Given list ", random_list)
    print(task_182(NUMBER, random_list))

    print("\nTask323: ")
    print(task_323(NUMBER))

    print("\nTask560: ")
    print(task_560())
