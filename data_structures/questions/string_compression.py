"""
Question 1.6
Implement a method to perform basic string compression using counts of repeated characters
"""


def compress_string(string):
    """
    Compresses string using basic compression in O(N) space and time

    Args:
        string - to compress
    Returns:
        Compressed string or original string if the compressed one is longer
    """

    count = 0
    compressed = []
    current = string[0]

    for letter in string:
        if letter == current:
            count += 1
        else:
            compressed.append("{}{}".format(current, count))
            current = letter
            count = 1

    # Flush the remaining
    compressed.append("{}{}".format(current, count))
    compressed_string = ''.join(compressed)

    if len(compressed_string) >= len(string):
        return string

    return compressed_string
