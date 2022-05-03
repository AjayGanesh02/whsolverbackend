from Trie import Trie
import pickle

tr = Trie()

with open("Dictionary/words_alpha.txt") as readfile:
    for word in readfile:
        tr.insert(word.strip())

with open("Dictionary/trie.pickle", "wb") as writefile:
    pickle.dump(tr, writefile)