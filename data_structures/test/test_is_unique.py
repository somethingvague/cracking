import random
import string
import time
import unittest

from data_structures.questions.is_unique import *

class TestIsUnique(unittest.TestCase):
    empty_string = ''

    @classmethod
    def setUpClass(cls):
        unique_string = list(string.ascii_letters)
        common_string = list(string.ascii_letters + string.ascii_letters)
        random.shuffle(unique_string)
        random.shuffle(common_string)
        cls.unique_string = unique_string
        cls.common_string = common_string

    def test_brute_force(self):
        self.assertTrue(brute_force(self.empty_string))
        self.assertTrue(brute_force(self.unique_string))
        self.assertFalse(brute_force(self.common_string))

    def test_sort_first(self):
        self.assertTrue(sort_first(self.empty_string))
        self.assertTrue(sort_first(self.unique_string))
        self.assertFalse(sort_first(self.common_string))

    def test_using_hash(self):
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
        long_string = ''.join(random.choice(string.ascii_letters) for _ in range(1000))
        self._time("Brute Force long string", brute_force, long_string)
        self._time("Sort First long string", sort_first, long_string)
        self._time("Using Hash long string", using_hash, long_string)

    @staticmethod
    def _time(desc, solution, arg):
        start = time.perf_counter()
        solution(arg)
        end = time.perf_counter()
        print("{:s} execution time: {:1.8f}".format(desc, end - start))
