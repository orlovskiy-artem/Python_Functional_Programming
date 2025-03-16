from typing import Callable


class Integer:
    def __init__(self, value: int):
        self.value = value


def is_pure(increment_fn: Callable[[Integer], Integer]) -> bool:
    n = 1
    number: Integer = Integer(n)
    number_1 = increment_fn(number) # equals 2
    number_2 = increment_fn(number) # equals 2
    number_3 = Integer(number.value+1) # equals 2
    number_4 = increment_fn(number_3) # equals 3
    test_1 = number_1.value == number_2.value
    test_2 = number_2.value == number_3.value and number_3.value == number_1.value
    test_3 = number_1.value != number.value and number_2.value != number.value
    test_4 = number_4.value == number_2.value+1
    return test_1 and test_2 and test_3 and test_4