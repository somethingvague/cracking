"""Question 1.9
Given an is_substring function, write a function which determines if a string is a rotation of another string
by only calling is_substring once
"""


def is_string_rotation(s1, s2):
    """Determines if a string is a rotation of another, O(N)

    Args:
          s1: the string
          s2: possible rotation
    Returns:
          True if s2 is a rotation of s1, False otherwise
    """

    if len(s1) == len(s2) and is_substring(s1 + s1, s2):
        return True

    return False


def is_substring(s1, s2):
    return s2 in s1
