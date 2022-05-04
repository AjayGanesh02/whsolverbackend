import unittest
import pickle
from trie import Trie, serializeTrie

class TestTrieMethods(unittest.TestCase):
    def setUp(self):
        self.tr = Trie()
    
    def test_dict_insert(self):
        with open("./Data/words_alpha.txt") as readfile:
            for word in readfile:
                self.tr.insert(word.strip())
        self.assertTrue(self.tr.search("test"))
        self.assertFalse(self.tr.search("test1"))

    def test_simple_insert(self):
        self.tr.insert("test")
        self.assertTrue(self.tr.search("test"))
        self.assertFalse(self.tr.search("other"))

    def test_multiple_insert(self):
        self.tr.insert("test")
        self.tr.insert("testlol")
        self.assertTrue(self.tr.search("test"))
        self.assertTrue(self.tr.search("testlol"))
        self.assertFalse(self.tr.search("other"))

    def test_prefix_search(self):
        self.tr.insert("testlol")
        self.assertTrue(self.tr.search("test", True))
        self.assertFalse(self.tr.search("test", False))
        self.assertTrue(self.tr.search("testlol", True))
        self.assertTrue(self.tr.search("testlol", False))
        self.assertFalse(self.tr.search("other", True))
        self.assertFalse(self.tr.search("other", False))

    def test_unserialize(self):
        with open("./Data/trie.pickle", "rb") as readfile:
            self.tr = pickle.load(readfile)
        self.assertTrue(self.tr.search("test"))

    def test_serialize(self):
        serializeTrie()
        self.assertTrue(True)
    
    def test_serialize_full(self):
        serializeTrie()
        with open("./Data/trie.pickle", "rb") as readfile:
            self.tr = pickle.load(readfile)
        self.assertTrue(self.tr.search("test"))