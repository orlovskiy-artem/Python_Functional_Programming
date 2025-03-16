from typing import Callable

from Essentials.TailFibonacci.tail_recursion import tail_call_optimized


def fibonacci_impl() -> Callable[[int], int]:
    @tail_call_optimized
    def fibonacci_tail(
            current_number: int,
            previous_number: int,
            depth: int
    ):
        if depth == 1:
            # return current number at the end of recursion
            return current_number
        # otherwise keep track of depth and compute args, pass them in tailed function
        return fibonacci_tail(
            current_number + previous_number,
            current_number,
            depth - 1
        )

    def fibonacci_base(number: int) -> int:
        if number < 2:
            return number
        # depth should be shifted by two to achieve the effect
        # for not returning the 1 as a result twice (seq: 0,1,0+1,1+1,...)
        return fibonacci_tail(
            current_number=1,
            previous_number=0,
            depth=number + 2
        )

    return fibonacci_base
