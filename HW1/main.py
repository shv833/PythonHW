"""This module let us check my algotasks:)"""

import random

from tasks.task_182 import task_182
from tasks.task_323 import task_323
from tasks.task_560 import task_560
from tasks.utils import (is_natural_number,
                        has_int_in_list)


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
