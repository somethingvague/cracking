"""Utility module for creating fixtures and other testing helpers"""

import string
import random
import time


def random_ascii_string(length=104):
    """Generates a random ascii string

    Args:
          length: length of string to be generated
    Returns:
        a random string of a given length based on the ascii character set
    """

    ascii_letters = list(string.ascii_letters)
    random_letters = [random.choice(ascii_letters) for _ in range(length)]
    return ''.join(random_letters)


def random_integers(length=500):
    """Generates a random list of integers of length

    Args:
        range: for each element
        length: size of return value
    Returns:
        random list of integers of length
    """

    return [random.randint(1, 10) for i in range(0, length)]


def profile(description, solution, *args):
    """Times the execution of a given is_unique implementation

    Args:
        description: short description of implementation of use case.
        solution: function to profile.
        *args: use case to be passed to the function
    """
    start = time.perf_counter()
    solution(*args)
    end = time.perf_counter()
    print("{:s} execution time: {:1.8f}".format(description, end - start))
