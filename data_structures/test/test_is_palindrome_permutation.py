import unittest
from data_structures.questions.is_palindrome_permutation import is_palindrome_permutation


class TestIsPalindromePermutation(unittest.TestCase):
    def test_is_palindrome_permutation(self):
        self.assertTrue(is_palindrome_permutation("abcabc"))
        self.assertTrue(is_palindrome_permutation("abcabcd"))
        self.assertFalse(is_palindrome_permutation("abcdab"))
        self.assertFalse(is_palindrome_permutation("abcdabdd"))

if __name__ == "__main__":
    unittest.main()
