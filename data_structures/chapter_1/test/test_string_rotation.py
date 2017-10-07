import unittest

from data_structures.chapter_1.questions.string_rotation import is_string_rotation


class TestStringRotation(unittest.TestCase):
    def test_string_rotation(self):
        self.assertTrue(is_string_rotation("waterbottle", "erbottlewat"))
        self.assertFalse(is_string_rotation("somestring", "stringother"))
        self.assertFalse(is_string_rotation("somestring", "strsomeing"))
        self.assertTrue(is_string_rotation("", ""))


if __name__ == "__main__":
    unittest.main()
