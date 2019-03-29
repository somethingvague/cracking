import unittest

from data_structures.c4_trees_and_graphs.structures.trie import Trie


class TestTrie(unittest.TestCase):
    def test_insert_raises_ValueError_if_key_contains_non_lowercase_ascii_characters(self):
        with self.assertRaises(ValueError):
            Trie().insert('abCd')

    def test_insert_inserts_key_in_tree(self):
        trie = Trie()
        trie.insert('battery')
        trie.insert('bat')
        trie.insert('banana')
        trie.print_contents()

        self.assertEqual(trie.number_of_words(), 3)

    def test_search_returns_true_when_key_is_present(self):
        key = 'supercalifragilisticexpialidocious'
        trie = Trie()
        trie.insert(key)
        self.assertTrue(trie.search(key))

    def test_search_returns_false_when_key_not_present(self):
        trie = Trie()
        trie.insert('alice')
        self.assertFalse(trie.search('bob'))
