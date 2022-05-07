import pickle
import collections

# Trie implementation from https://www.youtube.com/watch?v=FFQ-nbul6VY

class Trie(object):
    def __init__(self):
        self.children = collections.defaultdict(Trie)
        self.complete = False

    def insert(self, s):
        if not s:
            self.complete = True # if end of word, mark it as complete in trie
        else:
            self.children[s[0]].insert(s[1:]) # continue trie using first letter of word, pass along rest of word

    def search(self, s, prefix_check=False):
        if not s:
            return prefix_check or self.complete # if end of word and is still going, prefix must exist
        else:
            if s[0] in self.children:
                return self.children[s[0]].search(s[1:], prefix_check)
            else:
                return False


def serializeTrie():
    tr = Trie()

    with open("./Data/words_alpha.txt") as readfile:
        for word in readfile:
            if len(word) > 2:
                tr.insert(word.strip())

    with open("./Data/trie.pickle", "wb") as writefile:
        pickle.dump(tr, writefile)