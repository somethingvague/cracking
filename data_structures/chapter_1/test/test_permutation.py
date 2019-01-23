import random
import unittest

from data_structures.chapter_1.questions.permutation import sort_first, use_hash
from utils.utils import random_ascii_string, profile


class TestIsPermutation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.string = random_ascii_string()
        cls.permutation = cls.string
        random.shuffle(cls.permutation)
        cls.non_permutation = cls.string[:-1]

    def test_sort_first(self):
        """tests ``sort_first()`` implementation of the is_permutation module"""
        self.assertTrue(sort_first(self.string, self.permutation))
        self.assertFalse(sort_first(self.string, self.non_permutation))

    def test_use_hash(self):
        """tests ``use_hash()`` implementation of the is_permutation module"""
        self.assertTrue(use_hash(self.string, self.permutation))
        self.assertFalse(use_hash(self.string, self.non_permutation))

    def test_execution_times(self):
        """Times thae execution of each implementation in the module for a range of use cases"""

        profile("Sort First permutation", sort_first, self.string, self.permutation)
        profile("Sort First non permutation", sort_first, self.string, self.non_permutation)
        print()
        profile("Use Hash permutation", use_hash, self.string, self.permutation)
        profile("Use Hash non permutation", use_hash, self.string, self.non_permutation)

if __name__ == "__main__":
    unittest.main()
