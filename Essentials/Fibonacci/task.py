from typing import Callable


def fibonacci_impl() -> Callable[[int], int]:
    def func(number: int) -> int:
        if number == 0:
            return 0
        if number == 1:
            return 1
        return func(number - 1) + func(number - 2)

    return func
