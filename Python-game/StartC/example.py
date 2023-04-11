# |이 코드는 팩토리얼을 계산하는 함수를 제공하는 모듈입니다. 이 모듈은 doctest를 사용하여 테스트를 수행합니다.
# |
# |좋은 점:
# |- 함수에 대한 설명이 상세하게 주어져 있습니다.
# |- 함수의 입력값에 대한 예외 처리가 잘 되어 있습니다.
# |- doctest를 사용하여 함수의 테스트를 자동화하고 있습니다.
# |
# |나쁜 점:
# |- 함수의 이름이 모듈의 이름과 같습니다. 이는 모듈을 사용할 때 혼란을 줄 수 있습니다.
# |- 함수의 구현 방식이 비효율적입니다. 큰 수의 팩토리얼을 계산할 때 많은 시간이 소요됩니다. 이를 개선할 수 있는 방법이 있습니다.
"""
This is the "example" module.

The example module supplies one function, factorial().  For example,

>>> factorial(5)
120
"""

def factorial(n):
    """Return the factorial of n, an exact integer >= 0.

    >>> [factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> factorial(30)
    265252859812191058636308480000000
    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0

    Factorials of floats are OK, but the float must be an exact integer:
    >>> factorial(30.1)
    Traceback (most recent call last):
        ...
    ValueError: n must be exact integer
    >>> factorial(30.0)
    265252859812191058636308480000000

    It must also not be ridiculously large:
    >>> factorial(1e100)
    Traceback (most recent call last):
        ...
    OverflowError: n too large
    """

    import math
    if not n >= 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    if n+1 == n:  # catch a value like 1e300
        raise OverflowError("n too large")
    result = 1
    factor = 2
    while factor <= n:
        result *= factor
        factor += 1
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()