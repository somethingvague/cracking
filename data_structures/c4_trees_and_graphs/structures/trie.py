"""Custom Trie (Prefix Tree) implementation"""
import string


class TrieNode:
    """Node to be used in a Trie"""
    def __init__(self):
        self.children = [None] * 26  # Alphabet placeholder
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key):
        """Inserts a key into the Trie

        Args:
            key: key to insert into the Trie
        Raises:
            ValueError if the key contains non lower case ASCII characters
        """
        self._validate_key(key)

        node = self.root
        for char in key:
            alphabet_index = self._char_to_index(char)
            if node.children[alphabet_index] is None:
                node.children[alphabet_index] = TrieNode()
            node = node.children[alphabet_index]

        node.is_end_of_word = True

    def search(self, key):
        """Searches for a key in the Trie

        Args:
            key: key to search for
        Returns:
            True if the key is present, else False
        Raises:
            ValueError if the key contains non lower case ASCII characters
        """
        node = self.root
        for char in key:
            alphabet_index = self._char_to_index(char)
            if node.children[alphabet_index] is None:
                return False
            node = node.children[alphabet_index]

        return node.is_end_of_word

    def print_contents(self):
        """Prints all the words in the Trie"""
        self._print_contents(self.root, [])

    def _print_contents(self, node, prefix):
        for i in range(len(node.children)):
            child = node.children[i]
            if child is not None:
                prefix.append(self._index_to_char(i))
                if child.is_end_of_word:
                    print(''.join(prefix))
                self._print_contents(child, prefix)
                prefix.pop()

    def number_of_words(self):
        """Returns number of words present in the tree via recursive implementation"""
        return self._number_of_words(self.root, 0)

    def _number_of_words(self, node, count):
        for child in node.children:
            if child is not None:
                if child.is_end_of_word:
                    count += 1
                count = self._number_of_words(child, count)

        return count

    @staticmethod
    def _validate_key(key):
        for char in key:
            if ord('a') > ord(char) or ord('z') < ord(char):
                raise ValueError('Key must contain lower case ASCII characters only')

    @staticmethod
    def _char_to_index(char):
        """Returns the corresponding index in the alphabet array for the character"""
        return ord(char) - ord('a')

    @staticmethod
    def _index_to_char(index):
        """Returns the corresponding char for the index in the alphabet array"""
        return string.ascii_lowercase[index]
