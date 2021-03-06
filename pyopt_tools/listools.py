"""
Contains All list manipulation functions. Like sorting, removing duplicates, etc.
"""


def remove_duplicates(list1: list) -> list:
    """
    Removes duplicates from a list
    :param list1: list to remove duplicates from
    :return: list with duplicates removed

        Example:
            >>> remove_duplicates([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4])
            >>> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    return list(dict.fromkeys(list1))


def remove_duplicates_sort(list1: list) -> list:
    """
    Removes duplicates from a list with sorted elements also works with strings and numbers
    :param list1: list to remove duplicates from
    :return: list with duplicates removed

        Example:
            >>> remove_duplicates_sort([3, 1, 2 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4])
            >>> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    return list(set(list1))


def sort_list(list1: list, from_to_types: (tuple, list), sort_elements: bool = False) -> list:
    """
    Sorts a list for multiple types also sorts by elements if sort_elements is True

    warning: if there is a list in the list, that list will be sorted by type 'list' if type not specified it will be
    in the last position

    :param sort_elements: whether to sort the elements of the list or just sort by type (sort by type is default)
    :param list1: list to sort
    :param from_to_types: tuple or list with the type of the list elements to sort by
    :return: sorted list

        Example:
            >>> test_list = [2, 3, 2, 1, "string1", "string2", "string3",  3.3, 2.2]
            >>> sort_list(test_list, (str, int, float))
            >>> ['string1', 'string2', 'string3', 2, 3, 2, 1, 3.3, 2.2]
            >>> sort_list(test_list, (str, int, float), sort_elements=True)
            >>> ['string1', 'string2', 'string3', 1, 2, 2, 3, 2.2, 3.3]
    """
    end_list: list = []
    return_list = []
    curr_idx = 0
    types_separated_list = []
    if sort_elements:
        for types in from_to_types:
            types_item = []
            for item in list1:
                if types == type(item):
                    types_item.append(item)
            types_separated_list.append(types_item)
        sorted_list = []
        for item in types_separated_list:
            sorted_list.append(sorted(item))
        for item in sorted_list:
            for element in item:
                return_list.append(element)
    else:
        for types in from_to_types:
            for item in list1:
                if types == type(item):
                    return_list.insert(curr_idx, item)
                    curr_idx += 1
    for i in list1:
        if type(i) not in from_to_types:
            end_list.append(i)

    return return_list + end_list


def subdivide_by_type(list1: list, from_to_types: (tuple, list)) -> list:
    """
    Subdivides a list by types

    :param list1: list to subdivide
    :param from_to_types: tuple or list with the type of the list elements to subdivide by
    :return: list with the subdivided list

        Example:
            >>> test_list = [2, 3, 2, 1, "string1", "string2", "string3",  3.3, 2.2]
            >>> subdivide_by_type(test_list, (str, int, float))
            >>> [['string1', 'string2', 'string3'], [2, 3, 2, 1], [3.3, 2.2]]
    """
    return_list = []
    for types in from_to_types:
        types_item = []
        for item in list1:
            if types == type(item):
                types_item.append(item)
        return_list.append(types_item)
    return return_list
