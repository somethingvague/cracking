"""
Question 1.3
Write a method to replace all spaces in a string with '%20'
"""


def custom_urlify(string_list, true_length):
    """
    Strips and replaces spaces with '%20' with custom implementation.

    Args:
        string_list: list with characters to transform
        true_length: length of the stripped string
    Returns:
        string stripped and with strings replaced
    """

    new_index = len(string_list)

    for i in reversed(range(true_length)):
        if string_list[i] == " ":
            string_list[new_index - 3:new_index] = "%20"
            new_index -= 3
        else:
            string_list[new_index - 1] = string_list[i]
            new_index -= 1

    return string_list[new_index:]


def idiomatic_urlify(string_list):
    """
    Strips and replaces spaces with '%20' idiomatically.

    Args:
        string_list: list of characters to transform
    Returns:
        string stripped and with strings replaced
    """

    return list(''.join(string_list).rstrip().replace(" ", "%20"))
