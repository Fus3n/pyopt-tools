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
    """
    return n > -1 and sqrt(n) % 1 == 0