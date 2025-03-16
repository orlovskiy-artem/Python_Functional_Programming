from typing import Callable

from Essentials.Factorial.tail_recursion import tail_call_optimized


def factorial_impl() -> Callable[[int], int]:
    @tail_call_optimized
    def factorial_tail(current_number, depth) -> int:
        if depth == 1:
            return current_number
        return factorial_tail(current_number * depth, depth - 1)

    def factorial_base(number: int) -> int:
        if number < 2: return 1
        return factorial_tail(1, number)

    return factorial_base
