"""Question 1.5
There are 3 types of edits that can be performed on strings: insert a character, remove a character, replace a
character. Given two strings, write a function to check if they are one, or zero edits away
"""


def is_one_away(first, second):
    """Determines if two strings are one insertion, removal or replacement away from each other in O(N)

    Args:
        first: string
        second: string
    Returns:
        True if the second is "one away" from the first, False otherwise
    """

    if abs(len(first) - len(second)) > 1:
        return False

    # 'Insertion' is the inverse of 'removal'. For the insertion use case ensure 'first' is the smaller of the two
    #  strings so that we only need to handle 'insertion'
    if len(first) > len(second):
        first, second = second, first

    i = j = differences = 0

    while i < len(first) and j < len(second):
        if first[i] != second[j]:
            differences += 1
            if differences > 1:
                return False

            # If this is an insertion use case only increment j so we check the next character in 'second' against
            # the current character in 'first'
            if len(first) < len(second):
                j += 1
                continue

        i += 1
        j += 1

    return True
