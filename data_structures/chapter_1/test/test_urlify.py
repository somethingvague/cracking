import unittest

from data_structures.chapter_1.questions.urlify import custom_urlify, idiomatic_urlify
from data_structures.chapter_1.test.utility import profile


class TestURLify(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.string = "Some String With Spaces            "
        cls.expected = list("Some%20String%20With%20Spaces")
        cls.true_length = len(''.join(cls.string).rstrip())

    def test_custom_urlify(self):
        """Tests ``custom_urlify()`` from the urlify module"""

        self.assertEqual(custom_urlify(list(self.string), self.true_length), self.expected)

    def test_idiomatic_urlify(self):
        """Tests ``idiomatic_urlify()`` from the urlify module"""

        self.assertEqual(idiomatic_urlify(list(self.string)), self.expected)

    def test_execution_times(self):
        """Tests execution times of implementations"""

        profile("Custom urlify", custom_urlify, list(self.string), self.true_length)
        profile("Idiomatic urlify", idiomatic_urlify, list(self.string))

if __name__ == "__main__":
    unittest.main()
