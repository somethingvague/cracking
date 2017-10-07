import unittest

from data_structures.chapter_1.questions.one_away import is_one_away


class TestOneAway(unittest.TestCase):
    def test_is_one_away(self):
        # Equal
        self.assertTrue(is_one_away("abc", "abc"))

        # Replacement
        self.assertTrue(is_one_away("abc", "abx"))
        self.assertTrue(is_one_away("abc", "asc"))

        # Insertion
        self.assertTrue(is_one_away("abc", "abcd"))
        self.assertTrue(is_one_away("abcd", "abxcd"))

        # Removal
        self.assertTrue(is_one_away("abcd", "acd"))
        self.assertTrue(is_one_away("abcd", "bcd"))

        # Not One Away
        self.assertFalse(is_one_away("a", "abc"))
        self.assertFalse(is_one_away("abc", "axy"))
        self.assertFalse(is_one_away("abc", "abxy"))


if __name__ == "__main__":
    unittest.main()
