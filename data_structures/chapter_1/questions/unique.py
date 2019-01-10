"""Question 1.1
Implement an algorithm to determine if a string has all unique characters
"""


def brute_force(string):
    """Checks if a string has unique characters with brute force implementation which iterates and compares every pair
    of characters in the string, O(N^2) run time.

    Args:
        string: string to check for unique characters
    Returns:
        True if the characters in 'string' are unique, False otherwise
    """

    for i in range(len(string)):
        for j in range(len(string)):
            if i == j:
                continue

            if string[i] == string[j]:
                return False
    return True


def sort_first(string):
    """Checks if a string has unique characters by first sorting the string and compares adjacent characters. The
    underlying Timsort implementation gives O(N LogN) run time.

    Args:
        string: string to check for unique characters
    Returns:
        True if the characters in 'string' are unique, False otherwise
    """

    sorted_string = ''.join(sorted(string))
    for i in range(len(sorted_string) - 1):
        if sorted_string[i] == sorted_string[i + 1]:
            return False

    return True


def using_hash(string):
    """Checks if a string has unique characters by populating a dictionary of the letters. Runs in O(N) but requires
    the additional data structure.

    Args:
        string: string to check for unique characters
    Returns:
        True if the characters in 'string' are unique, False otherwise
    """

    letter_dict = {}
    for letter in string:
        if letter_dict.get(letter) is None:
            letter_dict[letter] = 1
        else:
            return False

    return True
