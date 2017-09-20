"""
Question 1.6
Implement a method to perform basic string compression using counts of repeated characters
"""


def compress_string(string):
    """
    Compresses string using basic compression in O(N) space and time.

    Args:
        string - to compress
    Returns:
        Compressed string or original string if the compressed one is longer
    """

    count = 0
    compressed = []

    for i, letter in enumerate(string):
        count += 1

        # Append character and count if next character is the end of the string
        # or if the next character is different to the current
        if i + 1 == len(string) or letter != string[i + 1]:
            compressed.append("{}{}".format(letter, count))
            count = 0

    compressed_string = ''.join(compressed)

    # Trade-off between compressing entire string first or checking size on each append in the loop
    if len(compressed_string) >= len(string):
        return string

    return compressed_string
