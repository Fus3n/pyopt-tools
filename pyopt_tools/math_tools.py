"""
Some math functions.
"""
from math import sqrt


def reverse_int(num: (int, str)) -> int:
    """
    returns a new reversed int from the given int or string with int
    :param num the number to reverse

    Example:
        >>> reverse_int(5678)\n
        >>> 8765

    """
    return int(str(num)[::-1])


def persistence(num: int) -> int:
    """
    returns the persistence of a number\
    :param num: the number to check
    :param num: the number to calculate the persistence of

    Example:
        >>> persistence(1234)
        >>> 2

    """
    string_num = str(num)
    count: int = 0
    while len(string_num) > 1:
        result = 1
        for i in string_num:
            result *= int(i)
        string_num = str(result)
        count += 1
    return count


def is_square(n: int) -> bool:
    """
    returns True if n is a perfect square, False otherwise
    :param n: the number to check

    Example:
        >>> is_square(4)
        >>> True
        >>> is_square(5)
        >>> False
    """
    return int(sqrt(n)) ** 2 == n


def is_hexagonal(n: int) -> bool:
    """
    returns True if n is a hexagonal number, False otherwise
    :param n: the number to check

    Example:
        >>> is_hexagonal(6)
        >>> True
        >>> is_hexagonal(5)
        >>> False
    """
    return n > -1 and sqrt(8 * n + 1) % 4 == 3


def is_triangular(n: int) -> bool:
    """
    returns True if n is a triangular number, False otherwise
    :param n: the number to check

    Example:
        >>> is_triangular(6)
        >>> True
        >>> is_triangular(5)
        >>> False
    """
    return n > -1 and sqrt(8 * n + 1) % 1 == 0


def is_pentagonal(n: int) -> bool:
    """
    returns True if n is a pentagonal number, False otherwise
    :param n: the number to check

    Example:
        >>> is_pentagonal(5)
        >>> True
        >>> is_pentagonal(6)
        >>> False
    """
    return n > -1 and sqrt(24 * n + 1) % 6 == 5


def is_prime(n: int) -> bool:
    """
    returns True if n is a prime number, False otherwise
    :param n: the number to check

    Example:
        >>> is_prime(5)
        >>> True
        >>> is_prime(6)
        >>> False
    """
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def lerp(a: float, b: float, t: float) -> float:
    """
    returns a linear interpolation between a and b at t
    :param a: the first value
    :param b: the second value
    :param t: the interpolation value

    Example:
        >>> lerp(0, 1, 0.5)
        >>> 0.5

    """
    return a + t * (b - a)


def clamp(value: float, n_min: float, n_max: float) -> float:
    """
    returns a clamped value between min and max
    :param value: the value to clamp
    :param n_min: the minimum value
    :param n_max: the maximum value

    Example:
        >>> clamp(12, 0, 10)
        >>> 10
    """
    return max(min(value, n_max), n_min)


def clamp01(value: float) -> float:
    """
    returns a clamped value between 0 and 1
    :param value: the value to clamp

    Example:
        >>> clamp01(12)
        >>> 1
    """
    return clamp(value, 0, 1)


def prime_factors(num: int) -> list:
    """
    returns a list of prime factors of a number
    :param num: the number to get the prime factors of
    :return: list of prime factors

    Example:
        >>> prime_factors(12)
        >>> [2, 2, 3]

    """
    factors = []
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            factors.append(i)
    if num > 1:
        factors.append(num)
    return factors
