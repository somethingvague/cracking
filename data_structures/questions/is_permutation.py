"""
Question 1.2
Given two strings, write a method to decide if one is a permutation of the other
"""


def sort_first(first, second):
    """
    Checks if the second string is a permutation of the first using a "sort first" implementation which sorts
    both strings then checks equality

    Args:
        first: some string
        second: another string which may or may not be a permutation of 'first'.
    Returns:
        True if the second string is a permutation of the first, False otherwise
    """

    first.sort()
    second.sort()
    return first == second


def use_hash(first, second):
    """
    Checks if the second string is a permutation of the first by populating a hash table of character -> count of the
    first string, then iterating over the second string and decrementing the count of the corresponding character
    in the hash table. Once complete the values of the hash should be all 0

    Args:
        first: some string
        second: another string which may or may not be a permutation of 'first'.
    Returns:
        True if the second string is a permutation of the first, False otherwise
    """

    count_by_char = dict()
    for char in first:
        if count_by_char.get(char) is None:
            count_by_char[char] = 1
        else:
            count_by_char[char] += 1

    for char in second:
        if count_by_char.get(char) is None or count_by_char.get(char) == 0:
            return False
        else:
            count_by_char[char] -= 1

    for count in count_by_char.values():
        if count != 0:
            return False

    return True
