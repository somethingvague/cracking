import unittest
from data_structures.c1_arrays_and_strings.questions.string_compression import compress_string


class TestStringCompression(unittest.TestCase):
    def test_compress_string(self):
        self.assertEqual(compress_string("aabcccccaaa"), "a2b1c5a3")

        unique_char_string = "abcdef"
        self.assertEqual(compress_string(unique_char_string), unique_char_string)

        redundant_compress_string = "aabbccddee"
        self.assertEqual(compress_string(redundant_compress_string), redundant_compress_string)


if __name__ == "__main__":
    unittest.main()
