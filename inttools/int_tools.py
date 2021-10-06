from math import sqrt

def reverse_int(int: int) -> int:
    """
    returns a new reversed int from the given int or string with int

    >> reverse_int(5678)
    >> 8765
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

def is_square(n: int) -> int:
    return n > -1 and sqrt(n) % 1 == 0