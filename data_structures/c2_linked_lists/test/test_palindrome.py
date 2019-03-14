import unittest

from data_structures.c2_linked_lists.questions.palindrome import is_palindrome_with_list, is_palindrome_with_stack
from utils.utils import create_linked_list


class TestPalindrome(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.even_length_list = create_linked_list([1, 2, 3, 3, 2, 1])
        cls.odd_length_list = create_linked_list([1, 2, 3, 2, 1])

    def test_is_palindrome_with_list_and_odd_length(self):
        self.assertTrue(is_palindrome_with_list(self.odd_length_list))

    def test_is_palindrome_with_list_and_even_length(self):
        self.assertTrue(is_palindrome_with_list(self.even_length_list))

    def test_is_palindrome_with_stack_and_odd_length(self):
        self.assertTrue(is_palindrome_with_stack(self.odd_length_list))

    def test_is_palindrome_with_stack_and_even_length(self):
        self.assertTrue(is_palindrome_with_stack(self.even_length_list))
