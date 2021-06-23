
from functools import lru_cache
import time


def fib(n: int) -> int:
    '''
        First approach using simple recursion
    '''
    if n < 2:
        return n
    return fib(n-2) + fib(n - 1)


def memoization(n: int) -> int:
    '''
        Using Memoization
        to solve the Fibonacci sequence
    '''
    memo: dict[int, int] = {0: 0, 1: 1}

    def fib_memo(n: int) -> int:
        if n not in memo:
            memo[n] = fib_memo(n - 1) + fib_memo(n - 2)
        return memo[n]

    return fib_memo(n)


@lru_cache(maxsize=None)
def fib_lru(n: int) -> int:
    '''
        Improved Memoization version
        using the LRU_CACHE decorator
        from Python
    '''
    if n < 2:
        return n
    return fib_lru(n - 2) + fib_lru(n - 1)


def iterative(n: int) -> int:
    '''
        Iterative approach for solving
        the Fibonacci sequence.
        Most efficient way.
    '''
    if n == 0:
        return n
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
    return next


def compare_performace(function, n):
    start = time.time()
    result = function(n)
    stop = time.time()
    print(f"{function.__name__} with n: {n} = {result} in {stop - start}")


if __name__ == '__main__':
    print(fib(4))
    print(memoization(4))
    print(fib(20))
    print(memoization(20))

    # print(fib(50)) NOOOOOOOO!!
    print(memoization(50))
    print(fib_lru(50))

    compare_performace(fib_lru, 100)
    compare_performace(iterative, 100)
