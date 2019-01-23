import random
import string
import unittest

from data_structures.chapter_1.questions.unique import brute_force, sort_first, using_hash
from utils.utils import random_ascii_string, profile


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
        """Tests the ``brute_force()`` method of the is_unique module"""

        self.assertTrue(brute_force(self.empty_string))
        self.assertTrue(brute_force(self.unique_string))
        self.assertFalse(brute_force(self.common_string))

    def test_sort_first(self):
        """Tests the ``sort_first()`` method of the is_unique module"""

        self.assertTrue(sort_first(self.empty_string))
        self.assertTrue(sort_first(self.unique_string))
        self.assertFalse(sort_first(self.common_string))

    def test_using_hash(self):
        """Tests the ``using_hash()`` method of the is_unique module"""

        self.assertTrue(using_hash(self.empty_string))
        self.assertTrue(using_hash(self.unique_string))
        self.assertFalse(using_hash(self.common_string))

    def test_execution_times(self):
        """Times the execution of each implementation in the module for a range of use cases"""

        profile("Brute Force unique string", brute_force, self.unique_string)
        profile("Sort First unique string", sort_first, self.unique_string)
        profile("Using Hash unique string", using_hash, self.unique_string)
        print()
        profile("Brute Force common string", brute_force, self.common_string)
        profile("Sort First common string", sort_first, self.common_string)
        profile("Using Hash common string", using_hash, self.common_string)
        print()
        long_string = random_ascii_string(10000)
        profile("Brute Force long string", brute_force, long_string)
        profile("Sort First long string", sort_first, long_string)
        profile("Using Hash long string", using_hash, long_string)

if __name__ == "__main__":
    unittest.main()
