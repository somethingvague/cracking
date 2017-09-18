"""
Question 1.4
Given a string, check if it is a permutation of a palindrome
"""

def is_palindrome_permutation(string):
    """
    Checks if a string is a permutation of a palindrome by populating a map and counting the occurrences of letters.
    O(N)

    Args:
        string: candidate palindrome permutation
    Returns:
        True if string is a palindrome permutation
    """

    letter_to_count = dict()

    for letter in string:
        letter_to_count[letter] = letter_to_count.get(letter, 0) + 1

    residual = 0
    for count in letter_to_count.values():
        residual += count % 2

    # there are can be a single letter with an odd character count when the palindrome is of odd length
    return residual <= 1

