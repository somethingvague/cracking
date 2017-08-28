import random
import string
import time
import unittest

from data_structures.questions.is_unique import *


class TestIsUnique(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        unique_string = list(string.ascii_letters)
        common_string = list(string.ascii_letters + string.ascii_letters)
        random.shuffle(unique_string)
        random.shuffle(common_string)
        cls.empty_string = ''
        cls.unique_string = ''.join(unique_string)
        cls.common_string = ''.join(common_string)

    def test_brute_force(self):
        """tests the ``brute_force()`` method of the is_unique module"""

        self.assertTrue(brute_force(self.empty_string))
        self.assertTrue(brute_force(self.unique_string))
        self.assertFalse(brute_force(self.common_string))

    def test_sort_first(self):
        """tests the ``sort_first()`` method of the is_unique module"""

        self.assertTrue(sort_first(self.empty_string))
        self.assertTrue(sort_first(self.unique_string))
        self.assertFalse(sort_first(self.common_string))

    def test_using_hash(self):
        """tests the ``using_hash()`` method of the is_unique module"""

        self.assertTrue(using_hash(self.empty_string))
        self.assertTrue(using_hash(self.unique_string))
        self.assertFalse(using_hash(self.common_string))

    def test_execution_times(self):
        self._time("Brute Force unique string", brute_force, self.unique_string)
        self._time("Sort First unique string", sort_first, self.unique_string)
        self._time("Using Hash unique string", using_hash, self.unique_string)
        print()
        self._time("Brute Force common string", brute_force, self.common_string)
        self._time("Sort First common string", sort_first, self.common_string)
        self._time("Using Hash common string", using_hash, self.common_string)
        print()
        long_string = ''.join(random.choice(self.unique_string) for _ in range(1000))
        self._time("Brute Force long string", brute_force, long_string)
        self._time("Sort First long string", sort_first, long_string)
        self._time("Using Hash long string", using_hash, long_string)

    @staticmethod
    def _time(desc, solution, arg):
        start = time.perf_counter()
        solution(arg)
        end = time.perf_counter()
        print("{:s} execution time: {:1.8f}".format(desc, end - start))


if __name__ == "__main__":
    unittest.main()
