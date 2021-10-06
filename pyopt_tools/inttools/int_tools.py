def revint(int):
    """
    returns a new reversed int from the given int or string with int

    >> revint(5678)
    >> 8765
    """
    return eval(str(int)[::-1])

def persistence(num):
    string_num =str(num)
    count: int = 0
    while len(string_num) > 1:
        result = 1
        for i in string_num:
            result *= eval(i)
        string_num = str(result)
        count += 1
    return count