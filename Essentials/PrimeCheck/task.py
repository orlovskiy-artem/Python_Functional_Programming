# import math
# from Essentials.Factorial.tail_recursion import tail_call_optimized

# can be optimized via tail call
# @tail_call_optimized
def is_prime(n: int) -> bool:
    if n==0 or n==1: return False
    import math
    def is_prime_rec(depth, number):
        if depth == math.ceil(math.sqrt(number)) + 1:
            return True
        if number % depth == 0:
            # print the possible case
            print(number // depth, depth)
            return False
        return is_prime_rec(depth + 1, number)

    # depth would start from 2, since it is better to
    # "filter out" by small numbers first than large ones
    # (meaning: better 2->n-1 than from n-1 to 2)
    return is_prime_rec(2, n)

