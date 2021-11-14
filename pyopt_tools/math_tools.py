# MIT License
# Copyright (c) 2021 FUSEN
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from math import sqrt


def reverse_int(int: int) -> int:
    """
    returns a new reversed int from the given int or string with int


    Example:\n
        >>> reverse_int(5678)\n
        >>> 8765
    """
    return eval(str(int)[::-1])


def persistence(num: int) -> int:
    """
    returns the persistence of a number

    :param num: the number to calculate the persistence of
    :return: the persistence of the number
    """
    string_num = str(num)
    count: int = 0
    while len(string_num) > 1:
        result = 1
        for i in string_num:
            result *= eval(i)
        string_num = str(result)
        count += 1
    return count


def is_square(n: int) -> bool:
    """
    returns True if n is a perfect square, False otherwise

    Example:\n
        >>> is_square(4)
        >>> True
        >>> is_square(5)
        >>> False
    """
    return n > -1 and sqrt(n) % 1 == 0


def is_hexagonal(n: int) -> bool:
    """
    returns True if n is a hexagonal number, False otherwise

    Example:\n
        >>> is_hexagonal(6)
        >>> True
        >>> is_hexagonal(5)
        >>> False
    """
    return n > -1 and sqrt(8 * n + 1) % 4 == 3


def is_triangular(n: int) -> bool:
    """
    returns True if n is a triangular number, False otherwise

    Example:\n
        >>> is_triangular(6)
        >>> True
        >>> is_triangular(5)
        >>> False
    """
    return n > -1 and sqrt(8 * n + 1) % 1 == 0


def is_pentagonal(n: int) -> bool:
    """
    returns True if n is a pentagonal number, False otherwise

    Example:\n
        >>> is_pentagonal(5)
        >>> True
        >>> is_pentagonal(6)
        >>> False
    """
    return n > -1 and sqrt(24 * n + 1) % 6 == 5


def is_prime(n: int) -> bool:
    """
    returns True if n is a prime number, False otherwise

    Example:\n
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

    Example:\n
        >>> lerp(0, 1, 0.5)
        >>> 0.5

    """
    return a + t * (b - a)


def clamp(value: float, n_min: float, n_max: float) -> float:
    """
    returns a clamped value between min and max

    Example:\n
        >>> clamp(12, 0, 10)
        >>> 10
    """
    return max(min(value, n_max), n_min)


def clamp01(value: float) -> float:
    """
    returns a clamped value between 0 and 1

    Example:\n
        >>> clamp01(12)
        >>> 1
    """
    return clamp(value, 0, 1)
